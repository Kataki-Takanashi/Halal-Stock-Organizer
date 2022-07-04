#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author acrazing - joking.young@gmail.com
# @version 1.0.0
# @since 2017-05-22 23:54:42
#
# Client.py
#
from same.Api import Api
from same.Channel import Channel
from same.Geo import Geo
from same.Sense import Sense
from same.User import User

version = '0.0.3'


class Client(Api):
    def __init__(self, **kwargs):
        super(Client, self).__init__(**kwargs)
        self.version = version
        self.channel = Channel(self)
        self.geo = Geo(self)
        self.sense = Sense(self)
        self.user = User(self)
