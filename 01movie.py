import pymysql

try:
    
    movnm=input('Enter movie name ')
    act=input('Enter actor ')
    acs=input('Enter actress ')
    ryr=int(input('Enter release year '))
    dct=input('Director name ')


    con=pymysql.connect(host='b39ypfpbn2wifz69zi63-mysql.services.clever-cloud.com',user='ujzmqwgblkrmfx3j',password='mOrNa0jsZjx3iIRvGe6P',database='b39ypfpbn2wifz69zi63')
    curs=con.cursor()

    curs.execute("insert into films values('%s','%s','%s',%d,'%s')" %(movnm,act,acs,ryr,dct))
    con.commit()
    print(' film added to cloud database')
    con.close()
except Exception as e:
    print('Error in data...cant insert',e)

