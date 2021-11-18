num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
num3 = int(input("请输入第三个数字："))

minnum = num1

if num2 < minnum:
    minnum = num2
   
if num3 < minnum:
    minnum = num3

print(minnum)


# 
#  a = 10  b = 20
#  a = 20  b = 10


chePiao = 1     # 用1代表有车票，0代表没有车票
daoLenght = 9     # 刀子的长度，单位为cm

if chePiao == 1:
    print("有车票，可以进站")
    if daoLenght < 10:
        print("通过安检")
        print("终于可以见到Ta了，美滋滋~~~")
    else:
        print("没有通过安检")
        print("刀子的长度超过规定，等待警察处理...")
else:
    print("没有车票，不能进站")
    print("亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~")
    
    
    
    