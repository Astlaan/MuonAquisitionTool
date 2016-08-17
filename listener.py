import time
import Adafruit_BBIO.GPIO as GPIO
import pymysql
import sys

class Listener:
	def __init__(self, multiprocessing=None):

		#Configurations
		self.path="data.txt"
		self.PIN = "P9_15" """This is the last AND output"""
		self.connection=self.connect()
		self.cur=self.connection.cursor()

		self.run(multiprocessing)

	def __del__(self):
		self.stop()
		self.connection.close()
		print("Shutting listener down.")

		#Save to file
	#object=open(path, "w")
	def log_event(self, a):
		timestamp=time.time()
		query="INSERT INTO Events (TimeStamp) VALUES FROM_UNIXTIME(" +timestamp+ ")"
		self.cur.execute(query)
		self.cur.close()
		#print check REMOVE WHEN FINISHED
		print("%s" % timestamp+"\n")


	def connect(self):
		user="AMU_user"
		password="AMUdlv"
		database="AMU_db"
		try:
			connection=pymysql.connect("localhost",user,password,database)
		except:
			print("Error connecting to the database.")
			sys.exit()
		return connection


	def start(self, elevation=None, latitude=None, longitude=None):  
		GPIO.setup(self.PIN, GPIO.IN)
		GPIO.add_event_detect(self.PIN,GPIO.RISING, self.log_event)
		print("Listening started")

	def stop(self):
		GPIO.remove_event_detect(self.PIN)
		GPIO.cleanup()
		print("Listening stopped")
		
	def run(self, multiprocessing):
		channel = input if not multiprocessing else multiprocessing.recv
		if multiprocessing:
			print("--Multiprocessing mode--") 

		while True:
			if channel()=="exit":
				break
			elif channel()=="start":
				self.start()
			elif channel()=="stop":
				self.stop()
			else:
				print("Error")
				break
		self.__del__()
	 

if __name__=='__main__':
	listener1=Listener()

	
"""The start method will have to receive the other fields to be saved into the database.
Changing the SQL query will also be required"""

#Eu meti "selfs" nos methods, ver se funcionou
