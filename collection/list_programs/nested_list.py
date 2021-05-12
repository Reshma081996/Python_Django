students=[[10,"ajay","bca",250],
          [11,"vijay","bca",240],
          [12,"sibin","bca",220],
          [13,"dino","mca",220],
          [14,"tom","mca",180],
          [15,"jain","mca",250]]
print(students)
print(students[1]) #[11, 'vijay', 'bca', 240]

#for stud in students:
    #print(stud[0])

for stud in students:
    if stud[3]>240:
        print(stud[1])

#find total of all marks
marks=0
for stud in students:
    marks+=stud[3]
print(marks)


# calculate bca and mca
mtotal,btotal=0,0
for stud in students:
    if stud[2]=="bca":
        btotal+=stud[3]
    else:
        mtotal+=stud[3]
print("bca total:",btotal)
print("mca total :", mtotal)