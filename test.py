#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import weiboo

def test(key):
	print(weiboo.search(key))

if __name__=='__main__':
	test('女权')
	test('7418114597')
