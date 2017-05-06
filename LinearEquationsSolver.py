#CS101 Project
#Linear equations solver with integer coefficients.
#Python 3.6

import sys, os

'''
The standard input textfile will contain an integer T in the first line, denoting the number of system of linear euations to be solved.
The first line of each test case will contain two numbers num_var and num_eq denoting the number of variables and number of equations.
The next num_eq lines will num_var+1 integers, denoting a equation of the form (a*x_1) + (b*x_2)=c, with a, b and c stored as values. 
'''

def GCD(num_1, num_2):
    if num_1==0:
        return num_2
    else:
        return GCD(num_2%num_1, num_1)
    

#Class for rational numbers
class irreducibleFractions:
    def update(self, num_1, num_2):
        if num_1==0 or num_2==0:
            self.num=0
            self.deno=1
        else:
            sign=True
            if num_1*num_2<0:
                sign=False
            if num_1<0:
                num_1=-num_1
            if num_2<0:
                num_2=-num_2
                    
            g=GCD(num_1, num_2)
            if not sign:
                self.num=-(num_1//g)
                self.deno=num_2//g
            
            else:
                self.num=num_1//g
                self.deno=num_2//g
    
    def __init__(self, num_1, num_2):
        self.num=num_1
        self.deno=num_2
        self.update(num_1, num_2)
            
                
    
    
    def __str__(self):
        return str(self.num)+'/'+str(self.deno)
    
    def getNum(self):
        return self.num
    
    def getDeno(self):
        return self.deno
    
        
        
        
    
    

def equationSolver(sys_Eq, rows, cols):
    #Converting the augmented matrix sys_Eq to row reduced echleon form
    row=rows
    col=cols+1 #Considering the augmented matrix.
    for i in range(row):
        for j in range(col):
            if sys_Eq[i][j]!=0:
                for y in range(row):
                    if y!=i:
                        coeff1=sys_Eq[y][j]
                        coeff2=sys_Eq[i][j]
                        for z in range(j, col):
                            sys_Eq[y][z]=coeff2*sys_Eq[y][z]-coeff1*sys_Eq[i][z]
                break
                    
    fracObjs=[]            
    for i in range(row):
        temp=[]
        for j in range(col):
            temp.append([])
        fracObjs.append(temp)
    
    for i in range(row):
        for j in range(col):
            if sys_Eq[i][j]!=0:
                num_2=sys_Eq[i][j]
        for j in range(col):
            fracObjs[i][j]=irreducibleFractions(sys_Eq[i][j], num_2)
    
    
    
    #Checking for consistency        
    for i in range(row):
        for j in range(col):
            if sys_Eq[i][j]!=0 and j==cols:
                return [False]
            elif sys_Eq[i][j]!=0 and j!=cols:
                break
                
                
    result=[]
    for x in range(cols):
        result.append('')
    
#    for x in range(row):
#        for y in range(col):
#            print(fracObjs[x][y])
        
    #Finding the values of num_var variables.
    for i in range(row):
        for j in range(cols):
            if fracObjs[i][j].__str__()!='0/1':
                for y in range(j+1, cols):
                    if fracObjs[i][y].__str__()!='0/1':
                        if result[j]!='':
                            result[j]+='+'
                        result[j]+='('+fracObjs[i][y].__str__()+' * x_'+str(y+1)+')'
                if fracObjs[i][cols].__str__()!='0/1':
                    if result[j]!='':
                        result[j]+='+'
                    result[j]+='('+fracObjs[i][cols].__str__()+')'
                break
    
    return [True]+result
        
                
            
            
            
            
            
filename=''
try:
    filename=sys.argv[1]
except:
    while filename=='' or not os.path.exists(filename):
        filename=input("Enter a valid input text filename:")
        

#Reading Input from the text file.
with open(filename, 'r') as ifile:
    inp=ifile.readlines()


wfile=open('Result of '+filename, 'w')

ctr=0
N=int(inp[ctr])
ctr+=1

#Solving N system of equations.
for x in range(N):
    num_var, num_eq=list(map(int, inp[ctr].split()))
    ctr+=1
    sys_Eq=[]
    for y in range(num_eq):
        sys_Eq.append(list(map(int, inp[ctr].split())))
        ctr+=1
    
    result=equationSolver(sys_Eq, num_eq, num_var)            
    wfile.write("Solution to Case #"+str(x+1)+": \n")
    
    if result[0]==False:
        wfile.write("The given system of equations is inconsistent.\n")
    else:
        for y in range(num_var):
            if result[y+1]=='':
                wfile.write('x_'+str(y+1)+ ' is free.\n')
            else:
                wfile.write('x_'+str(y+1)+' = '+result[y+1]+'\n')
    
    print('Completed Test Case '+str(x+1)+'!!\n')
    
        
    
wfile.close()        
    
        
    
    
