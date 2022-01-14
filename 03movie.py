
import pymysql

con=pymysql.connect(host='b39ypfpbn2wifz69zi63-mysql.services.clever-cloud.com',user='ujzmqwgblkrmfx3j',password='mOrNa0jsZjx3iIRvGe6P',database='b39ypfpbn2wifz69zi63')
curs=con.cursor()
nm=input(' Enter actor name: ')
curs.execute("select * from films where actor='%s'" %nm)
data=curs.fetchall()
print(data)