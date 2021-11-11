#字符串的编码转换
s='好运来祝你好运来'

#编码
print(s.encode(encoding='gbk'))
print(s.encode(encoding='utf-8'))

#解码
byte=s.encode(encoding="GBK")
print(byte.decode(encoding="gbk"))

byte=s.encode(encoding="UTF-8")
print(byte.decode(encoding="utf-8"))