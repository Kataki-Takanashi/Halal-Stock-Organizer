#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author acrazing - joking.young@gmail.com
# @version 1.0.0
# @since 2017-05-23 12:50:06
#
# Robot.py
#
from sys import argv

from same.Client import Client


class Robot:
    def __init__(self, sleep=2, timeout=10, **kwargs):
        self.client = Client(sleep=sleep, timeout=timeout, **kwargs)

    def like_all(self, channel_id, max_count=100):
        users = {self.client.user_id: True}
        count = 0
        next = None
        while next is not '' and count < max_count:
            data = self.client.sense.channel_list(channel_id, next=next).get('data', {})
            next = data.get('next', '')
            results = data.get('results', [])
            for item in results:
                user_id = item.get('user_id')
                if user_id in users:
                    continue
                users[user_id] = True
                user = item.get('user', {})
                if user.get('sex', 0) != 2:
                    self.client.log('omit for sex is not 2')
                elif item.get('is_liked', 0) == 0:
                    count += self.like_by_user(user_id)

    def like_by_user(self, user_id, max_count=2):
        next = None
        count = 0
        if user_id == self.client.user_id:
            return count
        profile = self.client.user.profile(user_id)
        if profile.get('is_staff', 0) == 1:
            self.client.log('omit staff user %s' % profile.get('username'), 'warning')
            return count
        if profile.get('sex', 0) != 2:
            self.client.log('omit for the sex is not 2')
            return count
        while next is not '':
            data = self.client.sense.user_list(user_id, next=next).get('data', {})
            next = data.get('next', '')
            results = data.get('results', [])
            for item in results:
                if item.get('is_liked', 0) == 0:
                    data = self.client.sense.like(item['id'])
                    if data.get('code', 0) != 0:
                        self.client.log(data, 'error')
                        raise AssertionError(data.get('detail'))
                    count += 1
                else:
                    count += 1
                if count >= max_count:
                    return count
        return count


if __name__ == '__main__':
    robot = Robot()
    method = getattr(robot, argv[1])
    print(method(*argv[2:]))
