#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author acrazing - joking.young@gmail.com
# @version 1.0.0
# @since 2017-05-23 02:17:09
#
# Geo.py
#
from same.Api import Module


class Geo(Module):
    def areas(self, path=None):
        return self.api.req('get', '/geo/areas', params={'path': path})

    def update(self, longitude, latitude, lbs=0):
        return self.api.req('post', '/geo/user/:user_id/update' % self.api.user_id, data={
            'longitude': longitude,
            'latitude': latitude,
            'lbs': lbs,
        })
