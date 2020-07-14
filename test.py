#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import weiboo

def test(key):
	for url, card in weiboo.search(key):
		print(url, weiboo.getCount(card))
	with open('tmp.txt', 'w') as f:
		f.write(str(weiboo.search(key)))

if __name__=='__main__':
	test('女权')
	test('7418114597')
