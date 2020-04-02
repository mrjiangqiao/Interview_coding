# -*-coding:utf-8-*-
import queue
import numpy as np
stack = queue.LifoQueue()
s = "((()))"
mul = 998244353
lens = len(s)
match_indice = [0]* lens
for i in range(lens):
    if s[i]=="(":
        stack.put(i)
    else:
        tmp_ind = stack.get()
        match_indice[i] = tmp_ind
        match_indice[tmp_ind] = i

def dp(x, y):
    if x+1==y:
        f[x,y,0,1] = f[x,y,0,2]=1
        f[x,y,1,0] = f[x,y,2,0]=1
        return
    if match_indice[x]==y:
        dp(x+1,y-1)
        for i in range(3):
            for j in range(3):
                if i!=1:
                    f[x,y,1,0] = (f[x,y,1,0]+ f[x+1,y-1,i,j])%mul
                if j!=1:
                    f[x,y,0,1] = (f[x,y,0,1]+ f[x+1,y-1,i,j])%mul
                if i!=2:
                    f[x,y,2,0] = (f[x,y,2,0] + f[x+1,y-1,i,j])%mul
                if j!=2:
                    f[x,y,0,2] = (f[x,y,0,2]  + f[x+1,y-1,i,j])%mul
    else:
        mid_pair = match_indice[x]
        dp(x,mid_pair)
        dp(mid_pair+1,y)
        for i in range(3):
            for j in range(3):
                for m in range(3):
                    for n in range(3):
                        if not((m==1 and n==1) or (m==2 and n==2)):
                            f[x,y,i,j] = (f[x,y,i,j]+(f[x,mid_pair,i,m]*f[mid_pair+1,y,n,j])%mul)%mul


f = np.zeros((800,800,3,3))
out_result = 0
dp(0,lens-1)
for i in range(3):
    for j in range(3):
        out_result = (out_result+int(f[0][lens-1][i][j]))%mul
print(out_result)