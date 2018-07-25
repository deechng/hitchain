#coding:utf-8

tokens = []
with open("tokens.txt","r") as fp:
	for line in fp.readlines():
		tokens.append(line.strip())

import Queue
TOKEN_POOL = Queue.Queue()
for token in tokens:
	TOKEN_POOL.put(token)

def get_token():
	if TOKEN_POOL.empty():
		return None
	token = TOKEN_POOL.get()
	# !!!!应该判断该token是否还有访问机会，否则再放回池子里
	return token

def push_token(token):
	TOKEN_POOL.put(token)



if __name__ == '__main__':
	print tokens
