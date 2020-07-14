#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'weibo_util'
import os

def getFile(fn):
	result = {}
	if not os.path.exists(fn):
		return result
	with open(fn) as f:
		for line in f.readlines():
			line = line.strip()
			if not line:
				continue
			key = ' '.join(line.split()[:-1])
			value = int(line.split()[-1])
			result[key] = value
	return result

class DB(object):
	def __init__(self, name): # first version, int value only
		self.fn = 'db/' + name
		self.items = getFile(self.fn)

	def update(self, key, value):
		self.items[key] = value
		self.save()

	def inc(self, key, value):
		oldValue = self.items.get(key, 0)
		self.update(key, oldValue + value)

	def get(self, key, default=None):
		return self.items.get(key) or default

	def save(self):
		lines = [key + ' ' + str(self.items[key]) for key in self.items]
		lines.sort()
		towrite = '\n'.join(lines)
		if not towrite:
			return
		os.system('mkdir db > /dev/null 2>&1')
		with open(self.fn + 'tmp', 'w') as f:
			f.write(towrite)
		os.system('mv %stmp %s' % (self.fn, self.fn))

def load(fn):
	return DB(fn)