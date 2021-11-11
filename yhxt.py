user1 = {"账号": "", "姓名": "", "密码": "", "地址": "", "存款余额": "", "开户行": "", }
def useradd(list):#注册
      for i in user1:
            sr=int(input("请输入"+i+":"))
            user1[i]=sr
      print(user1)
      print("注册成功")
      print("跳转登录页面")
      return list

def dl(ccq):#登录
      username=int(input("请输入您的账号:"))
      password=int(input("请输入您的密码:"))
      if username==ccq["账号"] and password==ccq["密码"]:
            print("登录成功，欢迎使用本系统！")
            print("-------------------------\n欢迎尊贵的",ccq["账号"],"用户使用本系统！！\n------------------------- ")
      elif username!=ccq["账号"] or password!=ccq["密码"]:
            print("您输入的账号或密码有误！")


def money(ccq):#存钱
      cq=int(input("请输入你存钱的数量"))
      ccq["存款余额"]=cq




def mian():
      while True:
            print("*1.登录   \n*2.注册  ")
            a=int(input("输入1或2选择登录和注册："))
            if a==1:
                  dl(ccq)
                  print("*1.存钱\n*2.取钱\n*3.转账\n*4.查询\n*5.Bye!")
                  money(ccq)
            elif a==2:
                  ccq=useradd(user1)
mian()