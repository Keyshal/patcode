num=int(input())
for i in range(num):
    tmp=input().split()
    if (int(tmp[0])+int(tmp[1]))>int(tmp[2]):
        print("Case #{}: true".format(i+1))
    else:
        print("Case #{}: false".format(i+1))
