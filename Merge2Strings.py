l1=[5,6,8,1,2,4,81,53,46]
l2=[1,40,11,9,5,3,7]
L3=l1+l2
for i in range(len(L3)):
    for j in range(i+1,len(L3)):
        if (L3[i]>L3[j]):
            L3[i],L3[j]=L3[j],L3[i]
print(L3)
