print("~~~~~~~~~~~~~~~~")
print("欢迎猜猜数字游戏")
print("~~~~~~~~~~~~~~~~")
a = 8
numble = int()
# count = -1
while  a != numble :
    numble = int(input("请开始输入幸运数字吧："))
    if a == numble:
        print("恭喜你，你成为了幸运儿了！！！")
    elif numble < 8:
        print("输入数字小了！")
    else:
        print("输入数字大了！")
