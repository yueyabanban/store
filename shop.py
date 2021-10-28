import pandas
#读取数据
df = pandas.read_excel("12月份衣服销售数据.xlsx")
#总金额=价格*销售量
df["总金额"]=df["价格/件"]*df["销售量/每日"]
print(df["总金额"].sum()) #总金额总和
#销售量总和/开始和结束的位置
rj=df["销售量/每日"].sum()/df["总金额"].count()#可选参数为在字符串搜索的开始与结束位置
print(rj)
yx=df["销售量/每日"]*30/df["库存数量"]
print(yx)

#"价格/件","库存数量","销售量/每日"的总和
sum_col = df[["价格/件","库存数量","销售量/每日"]].sum()
print(sum_col)
print("-------------------------------------")
print(df["价格/件"].sum())#"价格/件"总和
