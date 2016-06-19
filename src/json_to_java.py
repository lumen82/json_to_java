#!/usr/bin/python
#coding=utf-8
import json
from collections import OrderedDict

#生成成员变量
def generate_name(name):
        str = '\tprivate String ' + name + ';\n'
        return str;

#生成get 和 set 方法
def generate_getter(name):
	str = '\tpublic String get' + name.capitalize() + '() {\n'
	str += '\t\treturn this.' + name +'\n'
	str += '\t}\n'
	return str  
def generate_setter(name):
	str = '\tpublic void set' + name.capitalize() + '(String '+name + '){\n'
	str += '\t\tthis.' + name + ' = ' + name + '\n'
	str += '\t}\n'
	return str

sourceFile = open('temp','r')
jsonStr = sourceFile.next()
s = json.loads(jsonStr)
desFile = open('java.java', 'w')

#成员变量
for name in s.keys():
	desFile.write(generate_name(name))
desFile.write('\n')
#get and set founction
for name in s.keys():
	desFile.write('\n')
	desFile.write(generate_getter(name))
	desFile.write('\n')
	desFile.write(generate_setter(name))
desFile.write('\n')

sourceFile.close()
desFile.close()
