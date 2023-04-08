x,y,w,h = input().split()

w = int(w)
x = int(x)
y = int(y)
h = int(h)
short= int(x)
if(short > h-y):
    short = h-y
if(short > y):
    short = y
if(short >w-x):
    short = w-x
print(short)
