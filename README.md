# CS101-Project
# Apoorva Jakhar, Piyush Ravi, and Prakhar Jain

Our consits of solvers for a system of linear equations and sudoku, shuttle booking system, and currency convertor of listed currencies using Yahoo finance API. 

The file SudokuSolver.py, the solver for sudoku, takes input from a text file, say input_filename, and writes the ouput into another text file named as 'Result of [input_filename]'. 
Some test cases and their output is attached in a zipped folder named SudokuSolver_Testcases.zip.
The second test case of in1.txt in the zipped folder took about three hours to be solved. The test case is taken from Wikipedia and is designed to work against backtracking method. 
The empty spaces are marked by a 0 while the values already filled are with the number as there.

The file LinearEquationsSolver.py, the solver for a system of linear equations, takes input from text file, say input_filename, and writes the output into a text file named 'Result of [input_filename]'.
Some test cases and their result is attached in zipped folder named LinearEquationsSolver_TestCases.zip.

The shutlle booking systems consits of SignUp.html and form_backend.py.
SignUp.html is used to get user info for booking the shuttle, and then the user info is read by form_backend.py and output is shown on html. 

The currency convertor project consists of files, Currency_update.txt, currency_convertor.py and Yahoo! Finance Spreadsheet.xls.
The program currency_convertor.py reads from Currency_update.txt for getting the listed currencies and then uses Yahoo Finance API to fetch the latest available exchange rate.

Shuttle Scheduler
This web based application can be used to book the next shuttle at ashoka, on the front end part, HTML is used to gather important information about the person booking the shuttle. This information is sent to a python file which uses cgi libraries to incorporate web support. This python file uses SQL to fill out a table which is accessible to the admin, this table contains information of all the passengers. To avoid multiple entries and overbooking, the program checks for the same Ashoka id, if found, the booking is not done. 
We plan on increasing the scope of the code by incorporating auto generated emails 10 minutes before the shuttle time, we were able to get that part to work on a smaller scale, though the Id entered in the table of SQL wasn't directly usable. We made a small mass emailer which can be emailed to anyone requiring the prototype, till the time it is incorporated with the scheduler. 
For proper functioning, the python file has to be stored in the cgi-bin folder while the html file in the programs folder under XAMPP after being downloaded, when in running condition. 
https://www.apachefriends.org/download.html  - XAMPP can be downloaded here
This code works on safari browser on mac, it runs under local host web address. Rest is like a normal application.
You will be required to give admin rights to the cgi file using terminal if using mac (I dont know how it works for other OS)
There is an auto generated id which can be later used to see the total bookings. 
