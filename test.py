a = [1,2,3,'|',4,5,6,'|',1,1,4,5]
b = []
templst = []
for ele in a:
    if ele == '|':
        b.append(templst.copy())
        templst=[]
    else:
        templst.append(ele)
if templst !=[]:
    b.append(templst)
del templst

print(b)