st1={10,20,30,40}
st2={30,40,50,60,70,80}

#union
#10 ,20, 30, 40, 50,60,70, 80
uset=st1.union(st2)
print(uset)
# insertion order is not preserved-{70, 40, 10, 80, 50, 20, 60, 30}

#intersection
inter=st1.intersection(st2)
print(inter) #{40, 30}

#difference
diff=st1.difference(st2)
print(diff) #{10, 20}

