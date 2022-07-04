#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author acrazing - joking.young@gmail.com
# @version 1.0.0
# @since 2017-05-23 02:20:49
#
# Sense.py
#
import json

from same.Api import Module


class Sense(Module):
    def create(self, channel_id, txt=None, src=None, song_id=None, media_id=None, product_id=None, choices=None,
               audio_source_url=None, waveform=None, meta=None, video_source_url=None, sticker_url=None,
               cover_url=None):
        return self.api.req('post', '/sense/create', data={
            'channel_id': channel_id,
            'txt': txt,
            'src': src,
            'song_id': song_id,
            'media_id': media_id,
            'product_id': product_id,
            'choices': self.api.json(choices),
            'audio_source_url': audio_source_url,
            'waveform': waveform,
            'meta': self.api.json(meta),
            'video_source_url': video_source_url,
            'sticker_url': sticker_url,
            'cover_url': cover_url,
        })

    def delete(self, sense_id):
        return self.api.req('post', '/sense/%s/destroy' % sense_id)

    def fold(self, sense_id):
        return self.api.req('post', '/sense/%s/fold' % sense_id)

    def detail(self, sense_id):
        return self.api.req('get', '/sense/%s' % sense_id)

    def channel_list(self, channel_id, order='recent', _from=None, to=None, limit=None, next=None):
        params = {
            'from': _from,
            'to': to,
            'limit': limit,
        } if next is None else None
        next = '/channel/%s/%s/senses' % (channel_id, order) if next is None else next
        return self.api.req('get', url=next, params=params)

    def channel_newest_list(self, channel_id, next=None):
        return self.api.req('get', '/channel/%s/senses' % channel_id if next is None else next)

    def viewer_list(self, sense_id):
        return self.api.req('get', '/sense/%s/viewers' % sense_id)

    def id_list(self, id_list):
        return self.api.req('get', '/senses?ids=%s' % ','.join(id_list))

    def user_liked_list(self, next=None):
        next = '/user/%s/loves' % self.api.user_id if next is None else next
        return self.api.req('get', next)

    def user_list(self, user_id=None, next=None):
        next = '/user/%s/senses' % (user_id or self.api.user_id) if next is None else next
        return self.api.req('get', next)

    def user_channel_list(self, channel_id, user_id=None, next=None):
        next = '/user/%s/channel/%s/senses' % (user_id or self.api.user_id, channel_id) if next is None else next
        return self.api.req('get', next)

    def user_cate_list(self, cate, user_id=None, next=None):
        next = '/user/%s/senses/cate/%s' % (user_id or self.api.user_id, cate) if next is None else next
        return self.api.req('get', next)

    def user_cate_count(self, cate, user_id=None):
        return self.api.req('get', '/user/%s/senses/count/cate/%s' % (user_id or self.api.user_id, cate))

    def view(self, ids):
        return self.api.req('post', '/sense/view', data={
            'ids': ','.join(ids),
        })

    def like(self, sense_id):
        return self.api.req('post', '/sense/%s/like/create' % sense_id)

    def undo_like(self, sense_id):
        return self.api.req('post', '/sense/%s/like/destroy' % sense_id)

    def liked_user_list(self, sense_id):
        return self.api.req('get', '/sense/%s/likers' % sense_id)
