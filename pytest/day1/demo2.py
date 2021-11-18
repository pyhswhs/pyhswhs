name = "曹操"  # 字符串  string str  "" '123456'
age  = 18 # int number integer 整数  int
weight = 69.735 # float 小数

print("我的名字是" + name)

#TypeError: can only concatenate str (not "int") to str
#SyntaxError: invalid syntax 语法错误
#print("我的年龄是" age)

#%d 只能替换整数  %s 只能替换 字符串  %f 替换小数
print("我的名字是 %s" % name)
print("我的年龄是 %d" % age)
print("我的体重是 %f" % weight)
print("我的体重是 %.2f" % weight)


print("我的名字是 %s,我的年龄是 %d,我的体重是 %.2f" % (name, age, weight))

print("我的名字是 %s,\n我的年龄是 %d,\n我的体重是 %.2f" % (name, age, weight))

#\ 转义字符  \n 代表换行
print("\\")
print("\\n")