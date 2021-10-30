
# 数字求和
'''# n=input("请输入10个数")
it=list(n)
r=0
for i in it:
    r+=eval(i)
    print(r)'''


#三角形
'''x=int(input("请输入一个数"))
y=int(input("请输入一个数"))
z=int(input("请输入一个数"))

if (x+y>z) and (x+z>y)and(z+y>x):
    if x==y==z:
        print("等边三角形")
    elif(x==y or x==z or y==z):
        print("等腰三角形")
    elif (x*x+y*y==z*z)or(x*x+z*z==y*y)or(z*z+y*y==x*x):
        print("直角三角形")
    else:
        print("不规则三角形")
else:
    print("不是三角形")
'''

#使用random模块，产生50~150之间的数
'''import random
n=random.randint(50,150)
print(n)'''


#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''l=list(eval(input('10个数字用，隔开')))
avg=sum(l)/len(l)
a=sum(l)
v=max(l)
print("最大值",v)
print("平均值",avg)
print("总和",a)
'''

#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''name = "root"
password = "admin"
for i in range(0,5):
    username=input("请输入用户名:")
    userps=input("请输入用户密码:")
    if username==name and userps==password:
        print("登录成功")
    elif name!=username or password!=userps:
        if i <=3:
            print("用户名或密码错误")
        else:
            print("对不起，账户已锁定")'''



#编程实现下列图形的打印
'''a =input()
for i in range(int(a)//2+1):
    num = '*' * ((i+1)*2-1)
    print(num.center(int(a),' '))
'''
#使用while循环实现NxN乘法表的打印。
'''i=1
while i<=9:
    j=1
    while j<=i:
        print("%dx%d=%d"%(i,j,i*j),end='  ')
        j=j+1
    print('   ')
    i+=1
'''
#编程实现99乘法表的倒叙打印
'''for i in range(9,0,-1):
    for j in range(i,0,-1):
        print(str(i)+str("*")+str(j)+"="+str(i*j),end="\t")
    print()'''

#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
'''a=0
for i in range(0,100):
    a+=3
    if a>20:
        print("第",i,"天爬出来的")
        break
    a-=2
'''
#继续完成上午的猜数字游戏的需求功能。
#1.	添加计数打印功能
#2.	添加次数金币功能和锁定系统功能。
'''import random
print("猜字游戏")
q=1000
w=0
e=0
s=random.randint(0,10)
while True:
    a=int(input("请输入一个数字"))
    if a == s:
        w += 1
        q -= 100
        print("正确")
        break
    elif a>s:
        w+=1
        q -= 100
        print("你输入的过大，金额还剩",q,"已猜次数",w)
        if q==e:
            print("金额不足，系统锁定")
            break
    elif a<s:
        w+=1
        q-=100
        print("你输入的过小，金额还剩",q,"已猜次数",w)
        if q ==e:
            print("金额不足，系统锁定")
            break
print("金额还剩",q,"已猜次数",w)'''
#用循环来实现20以内的数的阶乘。
'''def recursion(n):
    if n==1:
        return 1
    else:
        return n*recursion(n-1)
list=[]
for i in range(1,21):
    list.append(recursion(i))
    print(sum(list))
Sum=0
for i in  renge(1,21):
    Sum+=recursion(i)
    print(Sum)
'''

#有以下两个数，使用+，-号实现两个数的调换。
'''a=56
b=78
print(a,b)
a,b=b,a
print(a,b)
'''

