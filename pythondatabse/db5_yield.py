import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database ='pythondecember'
)
def getdata():
    cursor=db.cursor
    sql="select * from movie"
    db.execute(sql)
    movies=cursor.fetchall()
    yield movies

    for movie in movies:
        print(movie)
#movies=getdata()
#print(movies)