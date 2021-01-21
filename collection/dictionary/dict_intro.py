#define {}
expense={"jan":20000,"feb":25000,"march":30000}
print(expense["march"])

#values stored in dict in the form of key value pair
#how do we fetch value from dictionary : using key
#is to possible to store duplicate key :key must be unique

#checking june20 in expense
print("jun20"in expense) #False

#adding new key value pairs in expenses
expense["june20"]=25000
print(expense)

#updating new wxpense
expense["march"]-=3000
print(expense["march"])