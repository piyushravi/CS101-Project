# CS101-Project
# Apoorva Jakhar, Piyush Ravi, and Prakhar Jain

Our consits of solvers for a system of linear equations and sudoku, shuttle booking system, and currency convertor of listed currencies using Yahoo finance API. 

The file SudokuSolver.py, the solver for sudoku, takes input from a text file, say input_filename, and writes the ouput into another text file named as 'Result of [input_filename]'.
Some test cases and their output is attached in a zipped folder named SudokuSolver_Testcases.zip.
The second test case of in1.txt in the zipped folder took about three hours to be solved. The test case is taken from Wikipedia and is designed to work against backtracking method.

The file LinearEquationsSolver.py, the solver for a system of linear equations, takes input from text file, say input_filename, and writes the output into a text file named 'Result of [input_filename]'.
Some test cases and their result is attached in zipped folder named LinearEquationsSolver_TestCases.zip.

The shutlle booking systems consits of SignUp.html and form_backend.py.
SignUp.html is used to get user info for booking the shuttle, and then the user info is read by form_backend.py and output is shown on html. 

The currency convertor project consists of files, Currency_update.txt, currency_convertor.py and Yahoo! Finance Spreadsheet.xls.
The program currency_convertor.py reads from Currency_update.txt for getting the listed currencies and then uses Yahoo Finance API to fetch the latest available exchange rate.
