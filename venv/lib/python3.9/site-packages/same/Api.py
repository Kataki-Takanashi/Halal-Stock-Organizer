#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author acrazing - joking.young@gmail.com
# @version 1.0.0
# @since 2017-05-22 23:55:15
#
# Api.py
#
from __future__ import unicode_literals
import json
import os
from sys import stderr
from threading import Thread

import requests
import time

DEFAULT_CACHE_FILE = os.path.join(os.path.expanduser('~'), '.same.json')


class Api:
    HOST = 'https://v2.same.com'

    def __init__(self, persist_file=DEFAULT_CACHE_FILE, flush=False, log_file=None, sleep=0, timeout=5, **config):
        self.log_file = stderr if log_file is None else open(log_file, 'a+', buffering=1)
        self.persist_file = persist_file
        self.user_id = 0
        self.secret = ''
        self.profile = {}
        self.config = config
        self.sleep = sleep
        self.timeout = timeout
        self.load()
        flush is True and self.flush()

    def load(self):
        if self.persist_file is None:
            return
        if os.path.isfile(self.persist_file) is False:
            return
        self.log('load session from %s' % self.persist_file)
        with open(self.persist_file, 'r') as f:
            data = json.load(f)
            self.user_id = data.get('user_id', 0)
            self.profile = data.get('profile', {})
            self.secret = data.get('secret', '')
            config = data.get('config', {})
            config.update(self.config)
            self.config = config
        return self

    def _persist(self):
        with open(self.persist_file, 'w+') as f:
            json.dump({
                'user_id': self.user_id,
                'profile': self.profile,
                'secret': self.secret,
                'config': self.config,
            }, f, indent=2)

    def persist(self):
        self.log('persist session to %s' % self.persist_file)
        thread = Thread(target=self._persist)
        thread.start()
        thread.join()
        return self

    def req(self, method='get', url='/', params=None, data=None, headers=None, auth=True, **kwargs):
        """
        
        :param method: 
        :param url: 
        :param params: 
        :param data: 
        :param headers: 
        :param kwargs: 
        :rtype: dict
        :return: 
        """
        self.log('request [%s] api: %s' % (method, url))
        headers = {} if headers is None else headers
        if self.secret:
            headers.update({
                'Authorization': 'Token %s' % self.secret,
            })
        url = self.HOST + url if url.startswith('/') else url
        s = requests.session()
        r = s.request(method, url, params=params, data=data, headers=headers, timeout=self.timeout, **kwargs)
        s.close()
        data = r.json()
        code = data.get('code')
        if code is not None and code == 403:
            self.expire()
            if auth is not False:
                raise PermissionError()
        if self.sleep != 0:
            time.sleep(self.sleep)
        return {} if data is None else data

    def login(self, mobile, password, email=None):
        data = self.req('post', '/user/login', data={
            'mobile': mobile,
            'password': password,
            'email': email,
        }).get('data', {})
        user = data.get('user', {})
        'user' in data and data.pop('user')
        user.update(data)
        self.user_id = user.get('id', 0)
        self.secret = user.get('token', '')
        self.profile = user
        self.persist()
        return self

    def expire(self):
        if self.user_id is 0:
            return
        self.log('session expired for user %s' % self.user_id)
        self.user_id = 0
        self.secret = ''
        self.profile = {}
        self.persist()
        return self

    def flush(self):
        if self.user_id is 0:
            return
        data = self.req('get', '/user/%s/profile' % self.user_id, auth=False).get('data', {})
        user = data.get('user', {})
        self.user_id = user.get('id', 0)
        self.profile = user
        self.persist()
        return self

    def use(self, secret):
        """
        :type secret: str
        :param secret: 
        :return: 
        """
        user_id = secret.rsplit('-', 1)[1]
        self.user_id = int(user_id)
        self.secret = str(secret)
        self.flush()
        return self

    def log(self, data, level='debug'):
        self.log_file.write('%s [%s] - %s\n' % (time.strftime('%y-%m-%d %H:%M:%S'), level.upper(), data))
        return self

    def __repr__(self):
        return 'same <%s>' % self.profile.get('username', self.profile.get('user_id', 'anonymous'))

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.log_file.closed is False:
            self.log_file.close()

    @staticmethod
    def json(obj):
        return json.dumps(obj, separators=(',', ':'), default=lambda x: x.__repr__())


class Module:
    def __init__(self, api):
        """
        :type api: Api
        :param api: 
        """
        self.api = api
