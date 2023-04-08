t = input()
t = int(t)
list = []
for i in range(0,t):
    list = input()# str "OXOOOXXXOXOX"
    counter =0
    total = 0
    for j in range(0,len(list)): #12
        if(list[j] == "O"): 
            counter += 1
            total = total+ counter
        else:
            counter = 0     
    print(total)
             


