import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database="pythondecember"

    )


cursor=db.cursor()
#sql='create table movie(id int,name varchar(200),year varchar(50),rating int)'
try:
    sql="insert into movie values(101,'lifeofpie','2007',5)"
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
db.close()