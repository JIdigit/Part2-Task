x = input()
r = list(x)
i=0
j=0
while 10>i:
    i+=1
    if j in range(0,len(x)+1):
        j+=1
    else:
        j=0
print(r[j])
# ili
# i=10
# j=list(input())
# index=10%len(j)
# print(j[index-1])