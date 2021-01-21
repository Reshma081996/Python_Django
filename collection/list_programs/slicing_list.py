lst=[15,20,30,35,40,45,50,55,60,65]
#     0  1  2  3  4  5  6  7  8  9
#   -10 -9 -8  -7 -6 -5 -4-3 -2  -1
#print(lst[1:3]) # excluding upper limit -[20, 30]
#print(lst[1:5]) #[20, 30, 35, 40]
#print(lst[:5]) # start from 0 to 5 - [15, 20, 30, 35, 40]
#print(lst[3:]) # start from 3 to last- [35, 40, 45, 50, 55, 60, 65]
#print(lst[::2]) # starting from o to last (since not given)by 2 steps-[15, 30, 40, 50, 60]
#print(lst[-1]) # negative indx -65
#print(lst[-3:])
# -ve from -3 to last -1 = [55, 60, 65]
#print(lst[:-2]) # from 0 to  -2 excluding tat [15, 20, 30, 35, 40, 45, 50, 55]
#print(lst[::-1]) # print list in reverse order

lst1=[4,5,10,4,3,2,1,9,8]
lst1.sort(reverse=True) # reverse=true ,descending order -[10, 9, 8, 5, 4, 4, 3, 2, 1]
print(lst1)
#print(sorted(lst1)) #[1, 2, 3, 4, 4, 5, 8, 9, 10]