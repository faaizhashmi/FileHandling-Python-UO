dic={}

a=500
b=550
c=400
d=550

dic['store1']=a
dic['store2']=b
dic['store3']=c
dic['store4']=d

val=max(dic,key=dic.get)
dic.pop(val)

val=max(dic,key=dic.get)