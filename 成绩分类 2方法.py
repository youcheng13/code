print ("-----------")
print ('成绩单分类|' )
print ("-----------")

A = int (input ("输入分数值："))
if 100 >= A >= 90:
    print ("=成绩是A")
else:
    if 80 <= A < 90:
        print ("成绩是B")
    else:
        if 60 <= A < 80:
            print ("成绩是C")
        else:
            if 0 <= A < 60 :
                print ("成绩是D,不及格")
            else:
                print ("错误输入值！请输入0到100之间的数值")