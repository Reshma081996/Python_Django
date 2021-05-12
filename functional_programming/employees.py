emplist=[
              {"id":10,"name":"christy","desig":"dataanalyst","sal":50000,"join":1980,"resign":1992},#12
              {"id":11,"name":"jhon","desig":"ba","sal":25000,"join":1980,"resign" :1992},#12
              {"id":12,"name":"sab", "desig":"dataanalyst","sal":80000,"join":1985,"resign":1990},
              {"id":13,"name":"tom","desig":"developer","sal":45000,"join":1989,"resign":1995}]
#for emp in emplist:
    #print(emp["sal"])
    #break
salary=max(list(map(lambda emp:emp["sal"],emplist)))
print(salary)

exp=list(filter(lambda emp:(emp["resign"]-emp["join"])>10,emplist))#[12, 12, 5, 6]->>map
print(exp)#id 10->12,11->12
#[{'id': 10, 'name': 'christy', 'desig': 'dataanalyst', 'sal': 50000, 'join': 1980, 'resign': 1992}, {'id': 11, 'name': 'jhon', 'desig': 'ba', 'sal': 25000, 'join': 1980, 'resign': 1992}]
