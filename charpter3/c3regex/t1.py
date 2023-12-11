import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*?Demo$', content,re.S)
print(result.group(1))
# 比较重要的一点，re.match对于一行字符串来说，是以开头开始的。
# ^ 用来指定内容进行匹配
# \s 用来匹配空格
# \d 用来匹配数字
# \w 用来匹配字母以及下划线
# .* .指示任意字符、* 表示重复前面的字符。
# .*? 像这样表示非贪婪匹配。
print(result)
print(result.group())
print('标记',result.group(1))
print('结果为',result.span())