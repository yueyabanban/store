import random
from DBUtils import update
from  DBUtils import  select
gs="中国工商银行"
gs_bank=[]

#开户重复验证
def gs_AddUser(account,username,password,country,province,street,door,money,gs):
    sql = "SELECT COUNT(*) FROM gsyh_yyds"
    data = select(sql,None, mode="all")

    if data[0][0] > 100:
        return 3

    sql1 = "SELECT * FROM gsyh_yyds where username = %s"
    param1 = [username]
    data1 = select(sql1, param1, mode="all")
    if len(data1) > 0:
        return 2

    sql2 = "insert into gsyh_yyds values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,username,password,country,province,street,door,money,gs]
    update(sql2, param2)
    return 1
#开户输入信息
def addUser():
    username = input("请输入您的姓名")
    password = input("请输入您的密码")
    country = input("请输入您的国籍")
    province = input("请输入您的省份")
    street = input("请输入您的街道")
    door = input("请输入您的门牌号")
    money = int(input("请输入您的余额"))
    account=random.randint(10000000,99999999)
    status=gs_AddUser(account,username,password,country,province,street,door,money,gs)
    if status == 3:
        print("银行库已经满了！请携带证件到其他银行办理！")
    elif status == 2:
        print("不允许重复开户！")
    elif status == 1:
        print("恭喜，开户成功！")
        info = '''
               ------------个人信息------------
               用户名 : %s
               账号：%s
               取款密码 : %s
               国籍：%s
               省份：%s
               街道：%s
               门牌号：%s
               余额:%s
               开户行名称：%s
           '''
        print(info % (username, account, password, country, province, street, door, money, gs))

#存钱验证
def save(savesr):
    sql="select username from gsyh_yyds where username =%s"
    param=[savesr]
    data=select(sql,param,mode="all")
    if len(data) == 1:
        return 1
    else:
        return False
#存钱输入信息
def save_Add():
    savesr=input("请输存的用户:")
    save_Money=int(input("请输入存入的金额"))
    saves=save(savesr)
    if saves ==1:
        sql2="UPDATE gsyh_yyds SET money = money + %s WHERE username = %s"
        param2=[save_Money,savesr]
        update(sql2,param2)
        print("添加成功")
#取钱验证
def si_Money_S(username,password,Money):
    sql="select username from gsyh_yyds where username = %s"
    param=[username]
    data3=select(sql,param,mode="all")
    if len(data3[0][0])==0:
        return 1
    sql1="select password from gsyh_yyds where username = %s"
    param1=[username]
    data4=select(sql1,param1,mode="all")
    if password != data4[0][0]:
        return 2
    sql2="select money from gsyh_yyds where username = %s"
    param2=[username]
    data5=select(sql2,param2,mode="all")
    if data5[0][0]<Money:
        return 3
    sql3 = "update gsyh_yyds set money = money - %s where username= %s"
    param3=[Money,username]
    update(sql3,param3)
    return 4

#取钱输入信息
def si_Money():
    username=input("请输入用户名:")
    password=input("请输入用户密码:")
    Money=int(input("请输入取钱的金额:"))
    s=si_Money_S(username,password,Money)
    if s==1:
        print("账号不存在!")
    elif s==2:
        print("密码不正确!")
    elif s==3:
        print("余额不足")
    elif s==4:
        print("取钱成功")

#转账验证
def acc(acc1,acc2,acc_Password,acc_Money):
        sql="select username from gsyh_yyds where username=%s or username=%s"
        param=[acc1,acc2]
        data=select(sql,param,mode="all")
        if len(data)==1:
            return 1

        sql1="select password from gsyh_yyds where username=%s"
        param1=[acc1]
        data1=select(sql1,param1,mode="all")
        if data1[0][0]!=acc_Password:
            return 2
        sql2="select money from gsyh_yyds where username=%s"
        param2 = [acc1]
        data2 = select(sql2, param2, mode="all")
        if data2[0][0]<acc_Money:
            return 3
        sql3 = "select money from gsyh_yyds where username=%s"
        param3 = [acc1]
        data3 = select(sql3, param3, mode="all")
        if acc_Money<=0:
            return 4
        # sql4 = "SELECT COUNT(*) FROM gsyh_yyds"
        # data4 = select(sql4, [], mode="all")
        # if len(data4[0][0])<2:
        #     return 5
        else:
            sql5="update gsyh_yyds set money = money-%s where username=%s"
            param5=[acc_Money,acc1]
            update(sql5,param5)
            sql6 = "update gsyh_yyds set money = money+%s where username=%s"
            param6 = [acc_Money, acc2]
            update(sql6, param6)
            return 6
#转账输入信息
def transfer_acc():
    acc1=input("请输入转出人的姓名")
    acc2=input("请输入转入人的姓名")
    acc_Password=input("请输入转出人的密码")
    acc_Money=int(input("请输入转出的金额"))
    t_Acc=acc(acc1,acc2,acc_Password,acc_Money)
    if t_Acc==1:
        print("-------------------\n转出人或转入人的姓名错误！\n-------------------")
    elif t_Acc==2:
        print("-------------------\n密码错误!\n-------------------")
    elif t_Acc==3:
        print("-------------------\n金额不足!\n-------------------")
    elif t_Acc==4:
        print("-------------------\n最低输入不能为0!\n-------------------")
    elif t_Acc==5:
        print("-------------------\n账户不足请再次创建新的用户！\n-------------------")
    elif t_Acc==6:
        print("转账成功")

#查询的验证
def querys(username,password):
    sql="select username from gsyh_yyds where username=%s"
    param=[username]
    data=select(sql,param,mode="all")
    if len(data)==0:
        return 1

    sql2="select password from gsyh_yyds where username = %s"
    param2=[username]
    data2=select(sql2,param2,mode="all")
    if data2[0][0] != password:
        return 2
    else:
        sql4="select * from gsyh_yyds where username=%s"
        param4=[username]
        data4=select(sql4,param4,mode="all")
        print(data4)
        return 3
#查询信息输入
def query():
    username=input("请输入用户名：")
    password=input("请输入密码:")
    d=querys(username,password)
    if d==1:
        print("该账户不存在!")
    elif d==2:
        print("密码错误")
    elif d==3:
        print()
        print("查询成功")
def welcome():
    print("欢迎使用中国工商银行自动存取系统！！"
          "\n1.开户"
          "\n2.存钱"
          "\n3.取钱"
          "\n4.转账"
          "\n5.查询"
          "\n6.Bye")
while True:
    welcome()
    sr=int(input("请输入业务编号:"))
    if sr==1:
        addUser()
    elif sr==2:
        save_Add()
    elif sr==3:
        si_Money()
    elif sr==4:
        transfer_acc()
    elif sr==5:
        query()
    elif sr==6:
        print("拜拜！")
        break
    else:
        print("输入错误，请重新输入")





















