#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author acrazing - joking.young@gmail.com
# @version 1.0.0
# @since 2017-05-23 13:47:54
#
# User.py
#
from same.Api import Module


class User(Module):
    def profile(self, user_id=None):
        """
        :param user_id: 
        :rtype: dict
        :return: 
        """
        user_id = self.api.user_id if user_id is None else user_id
        return self.api.req('get', '/user/%s/profile' % user_id).get('data', {}).get('user')
