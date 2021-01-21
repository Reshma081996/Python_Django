#lst=[2,6,4] op=[10,6,8]
#lst=[3,4,5] op=[9,8,7]

lst=[3,4,5]
total=sum(lst)
print(total)
op=list()
for num in lst:
    res=(total-num)
    op.append(res)
print(op)
#[1,2,3,4] imp=6 (4,2) op=(3,4)

