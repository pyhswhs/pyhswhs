#or


gao = input("高吗？ 请输入 Y/N:")
fu = input("富吗？ 请输入 Y/N:")
shuai = input("帅吗？ 请输入 Y/N:")


'''
if gao == "Y" and fu == "Y" and shuai == "Y":
    print("今晚有空")
else:
    print("洗澡去了")
'''

if gao == "Y" or fu == "Y" or shuai == "Y":
    print("今晚有空")
else:
    print("洗澡去了")