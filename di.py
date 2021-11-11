city={"北京":
          {"海淀":
                {"高校":["清华","北大"],
                 "公园":["香山","植物园"],
                 "博物馆":["军事博物馆","国家地质博物馆"]},
           "昌平":{"八达岭":["八达岭长城"],
                 "回龙观":["华联超市","中央戏剧学院回龙观校区"]
                 },
           "朝阳":{"公园":"玉渊潭公园"}
            },
      "上海":{"玩":"迪士尼"}
      }
shop={"货架A":["牙刷","牙膏","被子","枕头"],
      "货架B":["奶茶","巧克力","棉花糖","干脆面"],
      "货架C":["杯子","电话","雨伞","卫生纸"],
      }


def ad(data):
    for i in data:
        print(i,"",end="")
print("--------------------------欢迎来到时光旅社-------------------------------------")
for i in city:
    print(i)
xz=input("请输入要穿梭时空名称:")
if xz not in city:
    print("输入非法")
else:
    ad(city[xz])
    xz1=input("\n请输入想要穿梭地点的详细分区:")
    if xz1 not in city[xz]:
        print("输入非法")
    else:
        ad(city[xz][xz1])
        xz2=input("\n请输入该地址的范围")
        if xz2 not in city[xz][xz1]:
            print("输入非法")
        else:
            ad(city[xz][xz1][xz2])
            print("\n选择穿梭地址的地标，从左往右，数字0，1 代表需要穿梭的地址")
            xz3=int(input("请输入地标:"))
            if xz3 not in range(len(city[xz][xz1][xz2])):
                print("输入非法")
            else:
                print(city[xz][xz1][xz2][xz3])
            print("\n================================================")
            print("传送成功")
            print("正在载入商品购物系统")
            print("---------------------------------60%")
            print("----------------------------------------------90%")
            print("-------------------------------------------------------100%")
            print("商品系统载入完成")
            for o in shop:
                print(o)
            sp=input("请输入货架名称：")
            if sp not in shop:
                print("输入非法")
            else:
                ad(shop[sp])
                sp1=int(input("\n请输入0~3购买商品"))
                if sp1 not in range(len(shop[sp])):
                    print("输入非法")
                else:
                    print(shop[sp][sp1])
                    print("购买成功")

