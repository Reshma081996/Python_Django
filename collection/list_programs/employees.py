employees=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",25000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000]]

#print no of employyees in this company
num_of_employees=len(employees)
print("no of employees",num_of_employees)
#print how much salary company has to raise in moth
total_amount=0
for emp in employees:
    total_amount+=emp[3]
print(total_amount)

# group by desihnation
d_cnt, da_count,ba_count=0,0,0
for emp in employees:
    if emp[2]=="dataanalyst":
        da_count+=1
    elif emp[2]=="ba":
        ba_count+=1
    elif emp[2]=="developer":
        d_cnt+=1
print("no of datanalsyt",da_count)
print("no of ba",ba_count)
print("no of developer",d_cnt)

#print highest salaryed employee names
salary_list=[]
for emp in employees:
    salary_list.append(emp[3])
high=max(salary_list)
print(high)

for emp in employees:
    if emp[3]==high:
        print(emp)

#print emplooww who receises  lowest salary and desigantion is developer
#salary_list=[]
#for emp in employees:
    #salary_list.append(emp[3])
#low=min(salary_list)
#for emp in employees:
    #if emp[2]=='developer' and emp[3]==low:
        #print("lowest salaried employee:",emp)

dsalary_list=[]
for emp in employees:
    dsalary_list.append(emp[3])
mini=min(dsalary_list)
for emp in employees:
    if emp[3]==mini:
        print(emp)