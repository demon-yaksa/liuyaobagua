#coding=gbk
import random

raw_input("��Enter��ʼ")

arr = ("1", "0")

def drop():
	a = random.choice(arr)
	b = random.choice(arr)
	c = random.choice(arr)
	global part
	part = a+b+c
	if (part == "110") or (part == "011") or (part == "101"):
		mark1 = "һ"#����
		print mark1
	elif (part == "001") or (part == "100") or (part == "010"):
		mark2 = "--"#����
		print mark2
	elif (part == "111"):
		mark3 = "̫��(��س-����)"
		print mark3
	elif (part == "000"):
		mark4 = "̫��(��س-����)"
		print mark4

for i in range(6):
	drop()