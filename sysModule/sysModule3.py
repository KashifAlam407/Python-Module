### The sys moduel in python provides various functions and variable that are used to manipulate different parts of the python runtime environment. It allows operating on the interpreter as it provides access to the variable and functions that interact strongly with the interpreter. 


### Python sys.version
import sys
print(sys.version)   ## it gives the version of the interpreter that we are using to execute this code



##-----------------------------------------
### INPUT AND OUTPUT USING PYTHON SYS

###########################################
## 1. stdin, 2. stdout, 3. stderr

#1 stdin :-- it can be used to get inupt from the command line directly. It is used for standard input. it internally call the input() method. It also, automatically add '\n' after each sentence

#### This code reads lines from th standard input until the user enter 'q'. For each line, it prints "Input:" followed by the line. Finally, it prints "Exit".
import sys
for line in sys.stdin:   
    if 'q' == line.strip():
        break
    print(f"Input : {line}")

print("Exit")


###########################################
#2 stdout :-- A built-in file object that is analogous to the interpreter's standard output stream in python. stdout is used to display output directly to the screen console. Output can be of any form, it can be output from a print statement, an expression statement, and even a prompt direct for input. By default, stream are in text mode. In fact, wherever a print function is called within the code, it is first written to sys.stdout and then finally on to the screen.

#### This code will print the string"Geeks" to the standard output. The sys.stdout object represent the standard output stream, and the write() method writes the specified string to the stream.
import sys
sys.stdout.write('Geeks')


########################################
#3 stderr :-- Whenever an exception occurs in python it is written to sys.stderr.

#### This code will print the string "Hello World" to the standard error stream. The sys.stderr object represent error stream, and the print() function writes the specified strings to the stream.
import sys 
def print_to_stderr(*a): 
	print(*a, file = sys.stderr) 

print_to_stderr("Hello World") 


##-----------------------------------------
############################
import sys
n = len(sys.argv)
print("Total arguments passed:", n)
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:", end = " ")
for i in range(1, n):
	print(sys.argv[i], end = " ")
Sum = 0
for i in range(1, n):
	Sum += int(sys.argv[i])
	
print("\n\nResult:", Sum)


###########################
import sys 
age = 17
if age < 18: 
	sys.exit("Age less than 18")	 
else: 
	print("Age is not less than 18") 


##########################
import sys
print(sys.path)   # it print the system paths that python used to search for modules.


##########################
import sys
sys.path = []
# import pandas  # the code module will print an error message because the panda module is not in sys.path list.


##########################
import sys
print(sys.modules)   # return the name of the python modules that the current shell has imported


########################
import sys
a = 'Geeeeeeks'
print(sys.getrefcount(a))  # reference count (no. of distinct char)


#######################
import sys
print(sys.getwindowsversion())
print(sys.getwindowsversion()[1:4])  # printing by index no.



#------ MORE FUNCTIONS IN PYTHON SYS ------#

#sys.setrecursionlimit() ### it is used to set the maximum depth of the python interpreter stack to the required limit.

#sys.getrecursionlimit() method  ### it is used to find the current recursion limit of the interpreter or to find the maximum depth of the python interpreter stack.

#sys.settrace()  ### it is used for implementing debuggers, profilers and coverage tools. This is thread-specific and must register the trace using threading.settrace(). On a higher level, sys.settrace() registers the traceback to the Python interpreter.

#sys.setswitchinterval() method  ### it is used to set the interpreter's thread switch interval (in seconds).

#sys.maxsize()  ### it fetches the largest value a variable of data type Py_ssize_t can store.

#sys.maxint()  ### maxint/INT_MAX denotes the highest value that can be represented by an integer.

#sys.getdefaultencoding() method   ### it is used to get the current default string encoding used by the Unicode implementation.


