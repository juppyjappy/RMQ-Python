########################################
import math

#update(i,x):Aiをxに更新する
def update(i,x):
    k = i + num - 1
    while k >= 0:
        seg[k] = max(x,seg[k])
        k = (k-1)//2

#query(a,b,0,0,num):[a,b)の最大値
def query(a,b,k,l,r):
    if r <= a or b <= l:
        return -float("inf")
    elif a <= l and r <= b:
        return seg[k]
    else:
        return max(query(a,b,2*k+1,l,(l+r)//2),query(a,b,2*k+2,(l+r)//2,r))

######################################################

#sample input
n = 5
a = [3,4,2,5,6]

#初期化
#num : nより大きい最小の2のべき乗
num = 2**(int(math.log2(n))+1)
seg = [0]*(2*num-1)

#sample output
for i in range(n):
    update(i,a[i])

print(query(0,5,0,0,num))
print(query(1,4,0,0,num))
update(2,7)
print(query(1,4,0,0,num))