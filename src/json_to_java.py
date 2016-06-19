#!/usr/bin/python

import json

#生成变量名
def generate_name(name):
        str = 'private String ' + name + ';\n'
        return str;



sourceFile = open('temp','r')
jsonStr = sourceFile.next()
s = json.loads(jsonStr)
desFile = open('java.java', 'w')
for name in s.keys():
        desFile.write(generate_name(name))
sourceFile.close()
desFile.close()
