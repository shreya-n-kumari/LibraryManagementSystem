
"""this is for database connection"""

import mysql.connector

class DatabaseConnection(object):
	"""docstring for ClassName"""

	def __init__(self):
		#establishing the connection
		self.conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='college_library')

	def testConnection(self):
		#Creating a cursor object using the cursor() method
		cursor = self.conn.cursor()

		#Executing an MYSQL function using the execute() method
		cursor.execute("SELECT DATABASE()")

		# Fetch a single row using fetchone() method.
		data = cursor.fetchone()
		print("Connection established to: ",data)

	def getConnection(self):
			return self.conn

	def close(self):
		self.conn.close();
		print("database connection closed")

