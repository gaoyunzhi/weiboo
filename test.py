#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import weiboo
import time

def testSearch(key):
	for url, card in weiboo.search(key):
		print(url, weiboo.getCount(card))
	with open('tmp.txt', 'w') as f:
		f.write(str(weiboo.search(key)))

def testSearchUser(key):
	print(weiboo.searchUser(key))
	time.sleep(10)

if __name__=='__main__':
	# testSearch('女权')
	# testSearch('6520732164')
	# testSearchUser('澎湃新闻')
	# testSearchUser('5044281310')
	testSearchUser('摄影')
	testSearchUser('LGBT')
	testSearchUser('python')
	testSearchUser('书籍')
	testSearchUser('互受')
	testSearchUser('作家')
	testSearchUser('偏见')
	testSearchUser('公正')
	testSearchUser('公民')
	testSearchUser('写作')
	testSearchUser('剪报')
	testSearchUser('化学')
	testSearchUser('台湾')
	testSearchUser('女性')
	testSearchUser('女性作家')
	testSearchUser('女性故事')
	testSearchUser('女权')
	testSearchUser('妇女')
	testSearchUser('姐姐来了')
	testSearchUser('小说')
	testSearchUser('平权')
	testSearchUser('影像')
	testSearchUser('性别')
	testSearchUser('性少数')
	testSearchUser('技术')
	testSearchUser('摄影')
	testSearchUser('播客')
	testSearchUser('政治')
	testSearchUser('数学')
	testSearchUser('数学之恋')
	testSearchUser('数学之美')
	testSearchUser('数学之趣')
	testSearchUser('文学')
	testSearchUser('新闻')
	testSearchUser('日语')
	testSearchUser('旧金山')
	testSearchUser('李永乐')
	testSearchUser('湾区')
	testSearchUser('物理')
	testSearchUser('理论')
	testSearchUser('男性')
	testSearchUser('男权')
	testSearchUser('百合')
	testSearchUser('知识')
	testSearchUser('科学')
	testSearchUser('程序员')
	testSearchUser('耽美')
	testSearchUser('英语')
	testSearchUser('行动')
	testSearchUser('读书')
	testSearchUser('豆瓣')
	testSearchUser('香港')
	testSearchUser('工人')
	testSearchUser('工运')
	testSearchUser('女工')
	testSearchUser('工人运动')
	testSearchUser('劳工')
	

