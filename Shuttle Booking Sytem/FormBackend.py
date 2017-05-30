#!/usr/bin/python
import mysql.connector
from mysql.connector import errorcode
# Import modules for CGI handling 
import cgi, cgitb 
# Create instance of FieldStorage 

form = cgi.FieldStorage() 
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "shouut")
cursor=cnn.cursor()
name = form.getvalue('name')
ashoka_id = form.getvalue('ashoka_id')
e_number  = form.getvalue('e_number')
mobile = form.getvalue('mobile')
id=form.getvalue('id')
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Shuttle Bookings</title>"
print "</head>"
registers = 'SELECT e_number FROM seats'

cursor.execute(registers)
# Fetch all the rows in a list of lists.
result_register = cursor.fetchall()
print result_register
for i in result_register:
	
	if int(i[0])==int(e_number):
		print "User Exists"
		print "\n"
		print "<a href=/programs/SignUp.html>Re-Register</a>"    
		break
else:
	

	print "Welcome"
	addName="""INSERT INTO seats (name,ashoka_id,e_number,mobile) VALUES ('%s','%s','%s','%s')""" % (name, ashoka_id , e_number , mobile)
#addName="""INSERT INTO seats (name,ashoka_id,e_number,mobile) VALUES (abc,def,hgi,zxc)"""
	cursor.execute(addName)
	cnn.commit()
	cnn.close()
#print "<a href='/cgi-bin/getdata.py'> Check Availability </a>"
print "<body>"
#print "<h2> Hello %s %s %s %s %s %s %s %s </h2>" % (first_name,last_name,middle_name,mobile,day,month,year,qualification)

print "</body>"
print "</html>"
