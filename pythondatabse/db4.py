import mysql.connector

#establish connection with mysql
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    database="pythondecember",
    auth_plugin='mysql_native_password'
)
# step 3: create a cursor  (helps to communicate/transport  data in/out)
cursor=db.cursor()
sql='select * from movie'
cursor.execute(sql)
movies=cursor.fetchall()
for movie in movies:
    print(movie)