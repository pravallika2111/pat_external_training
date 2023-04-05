d={"hyd":"blr","blr":"che","che":"goi","goi":"mub"}
sou='mub'
cur=sou
des='goi'
l=[]
while(cur!=des):
    l.append(cur)
    try:
        cur=d[cur]
    except:
        print("NO such path")
        l.clear()
        
        break
if cur==des:
    l.append(cur)
   
print(l)