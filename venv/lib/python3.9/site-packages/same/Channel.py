#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author acrazing - joking.young@gmail.com
# @version 1.0.0
# @since 2017-05-23 01:48:00
#
# Channel.py
#

from same.Api import Module


class Channel(Module):
    def create(self, **data):
        return self.api.req('post', '/channel/create', data=data, auth=True)

    def detail(self, channel_id):
        return self.api.req('get', '/channel/%s/detail' % channel_id)

    def update(self, channel_id, **data):
        return self.api.req('post', '/channel/%s/update' % channel_id, data=data)

    def subscribe(self, channel_id):
        return self.api.req('post', '/channel/%s/book' % channel_id)

    def unsubscribe(self, channel_id):
        return self.api.req('post', '/channel/%s/cancel' % channel_id)

    def delete_announcement(self, channel_id):
        return self.api.req('delete', '/channel/%s/announcement' % channel_id)

    def subscribed_state(self, channel_id):
        return self.api.req('get', '/channel/%s/booked/state.json' % channel_id)

    def subscribed_users(self, channel_id):
        return self.api.req('get', '/channel/%s/booked/users' % channel_id)

    def check_create_params(self, **params):
        return self.api.req('get', '/channel/check', params=params)

    def check_create_permissions(self, mode):
        return self.api.req('get', '/channel/create/conditions', params={'mode': mode})

    def search(self, query, cate=None):
        return self.api.req('get', '/channel/search', params={'query': query, 'cate': cate})

    def payment_methods(self, channel_id):
        return self.api.req('get', '/channels/%s/payment/methods' % channel_id)

    def choose_post_cate(self, cate):
        return self.api.req('get', '/channels/for/post/%s' % cate)

    def online_count(self, channel_id):
        return self.api.req('get', '/imchannel/oluserscount?channel_id=%s' % channel_id)

    def online_users(self, channel_id):
        return self.api.req('get', '/imchannel/list?channel_id=%s' % channel_id)

    def updated_list(self):
        return self.api.req('get', '/latest/channels')

    def user_config(self, channel_id):
        return self.api.req('get', '/user/%s/channel/%s/config' % (self.api.user_id, channel_id))

    def user_post_count(self, channel_id):
        return self.api.req('get', '/user/%s/channel/%s/senses/count' % (self.api.user_id, channel_id))

    def index(self, contacts='none', channels='all', kv='no'):
        return self.api.req('get', '/user/%s/channels' % self.api.user_id, params={
            'contacts': contacts,
            'channels': channels,
            'kv': kv,
        })

    def user_posted_list(self):
        return self.api.req('get', '/user/%s/channels/write' % self.api.user_id)

    def user_owned_list(self):
        return self.api.req('get', '/user/%s/own/channels' % self.api.user_id)

    def add_announcement(self, channel_id, title, description, out_date):
        return self.api.req('post', '/channel/%s/announcement' % channel_id, data={
            'title': title,
            'description': description,
            'out_date': out_date,
        })

    def log_search(self, query, channel_id, cate=None):
        return self.api.req('get', '/channel/search/enter', params={
            'query': query,
            'channel_id': channel_id,
            'cate': cate,
        })

    def update_user_config(self, channel_id, config=None):
        return self.api.req('post', '/user/%s/channel/%s/update' % (self.api.user_id, channel_id), data={
            'config': self.api.json(config),
        })

    def update_announcement(self, channel_id, title, description):
        return self.api.req('post', '/channel/%s/announcement' % channel_id, data={
            'title': title,
            'description': description,
        })
