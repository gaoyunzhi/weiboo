#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import weiboo

def test(key):
	with open('tmp.txt', 'w') as f:
		for url, card in weiboo.search(key).items():
			print(url, weiboo.getHash(card))

if __name__=='__main__':
	test('女权')
	test('7418114597')
