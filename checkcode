# -*- coding:utf-8 -*-
str1 =[x for x in range(65,90)]        #生成存放小写字母对应ASCII码的列表
str2 = [x for x in range(97,122)]      #生成存放大写字母对应ASCII码的列表
charcter = str1 + str2                 #将2个列表组合在一起
str3 = [chr(x) for x in charcter]      #将列表中ASCII码转换为字符
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        #temp = chr(random.randint(65,90))  #验证码中仅包含小写字母
        temp = random.choice(str3)          #验证码中包含大小写字母
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)
