#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'weiboo'
import yaml
import cached_url
import urllib

def getSearchUrl(key):
	try:
		user = int(key)
		return 'https://m.weibo.cn/api/container/getIndex?type=uid&value=%d&containerid=107603%d' \
			% (user, user)
	except:
		content_id = urllib.request.pathname2url('100103type=1&q=' + key)
		return 'https://m.weibo.cn/api/container/getIndex?containerid=%s&page_type=searchall' % content_id

def search(key, force_cache=False, cookie=None, sleep=0):
	url = getSearchUrl(key)
	# one of the case we don't need cookie, let me check which one
	content = cached_url.get(url, 
		headers = {'cookie': cookie}, sleep = sleep)
	content = yaml.load(content, Loader=yaml.FullLoader)
	for card in content['data']['cards']:
		if 'scheme' in card:
			yielf card['scheme']