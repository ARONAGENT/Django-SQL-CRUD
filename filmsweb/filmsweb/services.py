import pymysql
class FilmsOperations:

    def reportFilms(self):
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="AVNS_jLvqn4KtNKeQMfTv6yn",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute("select * from films")
        data=curs.fetchall()
        con.close()
        return data

    def addnewfilm(self,nm,gen,lang,relyr,rate,desc):
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="AVNS_jLvqn4KtNKeQMfTv6yn",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute("insert into films (filmnm,genre,language,relyr,rating,description) values('%s','%s','%s','%s','%s','%s')" %(nm,gen,lang,relyr,rate,desc))
        con.commit()
        con.close()
        return "add new film Successfully"
    
    def retrivelangfilms(self,lang):
        dic={}
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="AVNS_jLvqn4KtNKeQMfTv6yn",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute("select * from films where language='%s'"%lang)
        data=curs.fetchall()
        dic["language"]=lang
        dic["searchresult"]=data
        con.close()
        return dic

    def retrivegenfilms(self,gen):
        dic={}
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="AVNS_jLvqn4KtNKeQMfTv6yn",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute("select * from films where genre='%s'"%gen)
        data=curs.fetchall()
        dic["genre"]=gen
        dic["searchgenresult"]=data
        con.close()
        return dic
    
    def updateRatingFilms(self,fid,rate):
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="AVNS_jLvqn4KtNKeQMfTv6yn",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute("update films set rating='%s' where filmid=%d"%(rate,fid))
        con.commit()
        con.close()
        return "films rating update Successfully"

    def deleteFilmById(self,id):
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="AVNS_jLvqn4KtNKeQMfTv6yn",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute("delete from films where filmid=%d "%id)
        con.commit()
        con.close()
        return "film deleted Successfully"
