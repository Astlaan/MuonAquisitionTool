import pymysql
import sys
from Database import DBFuncs
import time
import pyqtgraph
import numpy
from numpy import array
from PyQt4 import QtGui
from PyQt4 import QtCore

class Librarian:
	def __init__(self, test=False, parentBox=None):
		self.test=test
		#-----
		self.user = "AMU_user"
		self.password = "AMUdlv"
		self.database = "AMU_db"
		self.table="Events"
		#-----
		self.interval=15  #Number of past seconds to draw
		self.data=[[],[]]

		if not parentBox:
			print("WARNING - Parent box not set for Librarian's graph.")


		self.graph=pyqtgraph.PlotWidget(parentBox)
		self.graph.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
		self.graph.resize(self.graph.sizeHint())
		#self.graph.resize(500, 500)
		#self.graph.resize(500, 500)
		#self.data = numpy.random.normal(size=100)
		#self.data=[1,2,3]
		self.curve = self.graph.plot(x=self.data[0], y=self.data[1])

		if not test:
			self.connection = DBFuncs.EstablishConnection()
			self.connection.autocommit(True) #ULTIMA COISA QUE FIZ ONTEM
			self.cur=self.connection.cursor()
		else:
			print("-- Librarian test mode --")

	def setRange(value):
		self.interval=value
		self.refreshData()

	def refreshData(self, refreshgraph_flag=False):
		print("Refreshing data")
		if not self.test:
			self.data=self.getByDateInterval(time.time()-self.interval, time.time())
		if refreshgraph_flag:
			self.refreshGraph()

	def refreshGraph(self):
		print("Refreshing graph")
		#self.data = numpy.random.normal(size=100)
		#self.curve=self.graph.clear()
		#self.curve=self.graph.plot(self.data[0], self.data[1])
		self.curve.setData(x=self.data[0], y=self.data[1])


	def getByDateInterval(self, startdate, enddate): 
		if not self.test:
			a=self.cur.execute("select unix_timestamp(TimeStamp), count(*) as freq from Events where(TimeStamp between from_unixtime("+ str(int(startdate)) +") and from_unixtime("+ str(int(enddate)) +")) group by TimeStamp")
			if a==0:
				print("No data")
			data=[[],[]]
			for row in self.cur.fetchall():
				data[0].append(row[0]-enddate)
				data[1].append(row[1])		
			print("data[0]= ", data[0])
			print("data[1]= ", data[1])
			return data
		#self.cur.close() #CHECK WHICH FUNCTION TO FLUSH CURSOR



	def EstablishConnection(self):
		if not self.test:	
			try:
				connection = pymysql.connect("localhost",self.user,self.password,self.database)
				print("Successfully connected to database")
			except:
				print("Error connecting to the database.")
			#sys.exit()
		return connection


	def TerminateConnection(self):
		if not self.test:
			try:
				self.connection.close()
				print("Sucessfully closed the connection to the database.")
			except:
				print("Failed to close the connection to the database")
				#sys.exit()		
		
	def __del__(self):
		self.TerminateConnection()
		#stop timer


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