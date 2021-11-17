import xlrd

a = xlrd.open_workbook(filename=r"C:\Users\lenovo\Desktop\python学习笔记\day8\day08【excel表读写】\2020年每个月的销售情况.xls")
sum_money=0
for c in range(12):
    sheet=a.sheet_by_index(c)
    cols = sheet.ncols
    rows = sheet.nrows
    for i in range(1,rows):
        data=sheet.row_values(i)
        sum_money=sum_money+data[2]*data[4]#全年总金额

def q(t):#获取月份每件衣服的数量
    sheet = a.sheet_by_index(t)
    rr = sheet.nrows  # 获取行
    dict = {}
    for i in range(1, rr):
        data = sheet.row_values(i)
        dict[data[1]] = 0
    for j in range(1, rr):
        data = sheet.row_values(j)
        if data[1] in dict.keys():
            dict[data[1]] += data[4]
    return dict
def p():#每种衣服的月销售占比
    k=int(input("请输入对应的月份查询每月衣服的占比:"))
    qs=q(k)
    for i in qs:
        qs[i]=qs[i]/sum(qs.values())
    print("第",k+1,"个月的销售占比",qs)


iuy={}
#每种衣服的销售额占比
for ppl in range(12):
    sheet3 = a.sheet_by_index(ppl)
    ro = sheet3.nrows
    for jl in range(1,ro):
        data3=sheet3.row_values(jl)
        if data3[1] not in iuy.keys():
            iuy[data3[1]]=data3[2]*data3[4]
        elif data3[1] in iuy.keys():
            iuy[data3[1]]+=data3[2]*data3[4]

print("全年销售金额",sum(iuy.values()))
for oop in iuy:
    iuy[oop]=iuy[oop]/sum(iuy.values())
print("全年衣服销售金额占比",iuy)

op=0
ll={}
def y():#每种衣服的销售占比
    for i in range(12):
        rt=q(i)
        for j in rt:
            if j not in ll:
                ll[j]=rt[j]
            elif j in ll:
                ll[j]+=rt[j]
    pp=sum(ll.values())
    for k in ll:
        ll[k]=ll[k]/pp
    print("每种衣服销售的占比")
    print(ll)
    for oi in ll:
        if ll[oi]==min(ll.values()):
            print("那个衣服全年销售最低:")
            print(oi)
        elif ll[oi]==max(ll.values()):
            print("全年最畅销的衣服")
            print(oi)

y()
p()
