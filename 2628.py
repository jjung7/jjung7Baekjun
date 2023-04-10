row,col = input().split()
row = int(row)
col = int(col)
list_row = []
list_col = []
T = int(input())
maxrow = 0
maxcol = 0
for i in range(0,T):
    
    x,y = input().split()
    x = int(x)
    y = int(y)
    if (x == 1):
        maxrow = y
    elif(x == 0):
        maxcol = y
    
    list_row.append(maxrow)
    list_col.append(maxcol)
    list_row.sort()
    list_col.sort()
    
    col1 = list_col[0]
    row1 = list_row[0]
    for j in range(0,len(list_row)):
        if(j + 1 == len(list_row)):
            if(row1 < row - list_row[j]):
                row1 = row - list_row[j] 
        elif(list_row[j+1] - list_row[j] > row1):
            row1 = list_row[j+1] - list_row[j]
           
    for u in range(0,len(list_col)):
        if(u + 1 == len(list_col)):
            if(col1 < col - list_col[u]):
                col1 = col - list_col[u]    
        elif(list_col[u+1] - list_col[u] > col1):
            col1 = list_col[u+1] - list_col[u]
           
print(row1 * col1)

    # if(row != 0):


