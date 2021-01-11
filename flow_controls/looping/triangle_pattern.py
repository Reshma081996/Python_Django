i=0
for row in range(1,5):#1,2
    for col in range(1,8):# 1 in(1,8)-true, 2 in(1,8)-t,3 in(1,8)-t, 4 in(1,8)t,5 in(1,8)=t,6,7
        #2-1 in(1,8)-true, 2 in(1,8),3 in(1,8)-t,4in(1,8)-t,5 in(1,8)
        if(row==4) |(row+col==5) | (col-row==3):#1-(col4+(row1)=5),2-(row2+col3),2-(col5-row2=3)
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()

#s1s2s3*s5s6s7
#s1s2*s4*