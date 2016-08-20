import time
import pymysql
import sys

test1=False
try:
	import Adafruit_BBIO.GPIO as GPIO
except ImportError:
	test1=True

class Listener:
	def __init__(self, multiprocessing=None, test=False):

		#Configurations
		self.path="data.txt"
		self.PIN = "P9_15" """This is the last AND output"""
		self.test=test
		# if test:
		# 	print("-- Listener test mode --")

		self.run(multiprocessing)



	def __del__(self):
		self.stop()
		if not self.test:
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
		#if not self.test:
		#	GPIO.setup(self.PIN, GPIO.IN)
		#	GPIO.add_event_detect(self.PIN,GPIO.RISING, self.log_event)
		print("Listening started")

	def stop(self):
		#if not self.test:
		#	GPIO.remove_event_detect(self.PIN)
		#	GPIO.cleanup()
		print("Listening stopped")
		
	def run(self, multiprocessing):
		if multiprocessing:
			print("--Multiprocessing mode--") 	
		
		channel = input if not multiprocessing else multiprocessing.recv
			
		while True:
			try:
				command=channel()
			except:
				print("Listening - Could not get command from channel")
				sys.exit()
			if command=="exit":
				break
			elif command=="start":
				self.start()
			elif command=="stop":
				self.stop()
			else:
				print("Error")
				break
		self.__del__()
	 

if __name__=='__main__':
	if len(sys.argv)==2:
		test1=True
	listener1=Listener(test=test1)


	
"""The start method will have to receive the other fields to be saved into the database.
Changing the SQL query will also be required"""

#Eu meti "selfs" nos methods, ver se funcionou
