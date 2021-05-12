#step1 import mysql.connector
import mysql.connector

#establish connection with mysql
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password'


)
# step 3: create a cursor  (helps to communicate/transport  data in/out)

cursor=db.cursor()

sql='select version()'
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()