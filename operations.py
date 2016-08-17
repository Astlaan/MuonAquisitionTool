import pymysql
import sys
from Database import DBFuncs

class Librarian:
	def __init__(self):
		self.user = "AMU_user"
		self.password = "AMUdlv"
		self.database = "AMU_db"
		self.table="Events"

		self.connection = DBFuncs.EstablishConnection()
		self.cur=self.connection.cursor()


	def EstablishConnection():
		#login information
		user = "AMU_user"
		password = "AMUdlv"
		database = "AMU_db"
		#connecting with MySQL to access the database
		try:
			connection = pymysql.connect("localhost",user,password,database)
		except:
			print("Error connecting to the database.")
			sys.exit()
		return connection


	def getByDateInterval(self, startdate, enddate): #ONLY WORKS IN UNIX ATM, CHECK THE UNIX TIMESTAMP PART
		self.cur.execute("select unix_timestamp(TimeStamp), count(*) as freq from Events where(TimeStamp between " + startdate + " and " + enddate + ") group by TimeStamp")
		self.data = self.cur.fetchall()
		#self.cur.close() #CHECK WHICH FUNCTION TO FLUSH CURSOR

	def TerminateConnection(self):
		try:
			self.connection.close()
			print("Sucessfully closed the connection to the database.")
		except:
			print("Failed to close the connection to the database")
			sys.exit()		
		
	def __del__(self):
		self.TerminateConnection()


"""Useful python time functions"""
#datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") get time now
#time.strftime('%Y-%m-%d %H:%M:%S') does the same
#2010-01-30 14:15:55 (SQL format)

"""Get epoch time from mysql (let it do the hard work):"""
#select unix_timestamp(fieldname) from tablename;

"""Get frequency of each TimeStamp"""
#select TimeStamp, count(*) freq from Events group by TimeStamp


"""PySQLPool code..."""
# self.connection = PySQLPool.getNewConnection(username=self.user, password=self.password, host='localhost', db=self.database)
# self.query = PySQLPool.getNewQuery(connection)
# self.data=[]

"""Unused SQL Functions"""
# ("SELECT * FROM " + self.Table + " WHERE (date_field BETWEEN %s AND %s)" %(startdate, enddate)
# select TimeStamp, count(*) as freq from Events where(TimeStamp between '2000-01-01 20:20:20' and '2000-01-01 20:20:20') group by TimeStamp
# UNIX_TIMESTAMP(NOW())