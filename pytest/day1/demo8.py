

score = input("请输入您的分数：")

score = int(score)

if score > 90 and score <= 100:
    print("优秀")
elif score > 80 and score <= 90:
    print("良好")
elif score > 70 and score <= 80:
    print("可以")
else:
    print("天才")