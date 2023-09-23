#!/usr/bin/env python
# coding: utf-8

# # <center><font color=green>Python Primer </font> </center>  
# ### <font color=red> **Important** </font>
# 
# ### Save this file with your initials and last two digits of ID number appended to file name like "Module 1 Assignment, DOE Jane 25, H02 IPYNB" before submitting it. 
# ### In addition, put a comment at the beginning of each code block to explain it with the same initials and digits. I have put one at the beginning as an example for you to follow. Do not forget to change it. 
# ### Finally, you will name all variables similarly: for instance, x = 3 below will be modified as xJD54 = 3. 
# ### If your initials and digits appear in any other student's submission or if another student's initials and digits appear in your submission you will be degraded one letter and I will file your submission to the Academic Integrity Office.
# ### Be sure to run all the codes before you submit your assignment 

# ### 1. Comments 
# 
# Comments help a lot to take notes while coding. They are so useful to remind you and other coders of what you are doing.

# <font color=red> **Run the following code by simply clicking on the "Run this cell" beside the block** </font>

# In[ ]:


# MO54 This is a simple comment to exemplify how the comments are placed in Pyhton
# This is a comment


# <font color=red> **Write a comment below to express your first impression about this course and run it. Remember
#     that you are supposed to put a comment at the top of each code block with your initials and digits** </font> 

# In[17]:


#YC95
# I am very much interested to run pythan. This will be very helpful for me as 


# print("Welcome to ADTA 5230 Data Mining analytics 2 Course ")


# ## 2. Print text on screen

# In[1]:


print ("Hello World")


# <font color=red> **Write a command below to print "Hello Professor Orhan!"** </font>

# In[20]:


#YC95
print("Hello Professor Orhan!")


# ## 3. Identifiers, Keywords, and Data Types

# ### 3.1 Data Containers
# ###### Variables are data containers whose values are likely to be changed along the course of executing a program.

# #### Variable/Identifier x:
# 
#  - x is an identifier. It is a ***variable.***
#  - its value is 3: 3 is ***data***
#  - The variable (identifier) x is the ***data container*** that contains the piece of data "3".
#  - ***Data type*** of x is "int"
# 
# Here is an example
# 
#  <font color=red> **Run the following code:** </font>

# In[11]:


# x is a name of a variable. x is an identifier.
x = 3

print ("x is a variable. It is an identifier. Its value is: ",x, "\n")
print("Data type of x: ", type (x), '\n')

#stdName is a name of a variable that represents the name of a student.
#stdName is an identifier

stdName = "John Smith"

print ("stdName is a variable. It is an identifier. Its value is: ", stdName, "\n")
print("Data type of stdName: ", type (stdName), '\n')


# <font color=red> **Define another variable y and set it equal to last three digits of your ID number. Define another variable for student name (call it stname) and set it equal to your full name. Modify the block code above with these two new variables (y and stname) and run it. Be careful about naming variables exlained at the top, i.e. y should appear as yMO354, for instance.** </font>

# In[94]:


#YC95
# y is a name of a variable. y is an identifier.
y = "095"

print ("y is a variable. It is an identifier. Its value is: ",y, "\n")
print("Data type of y: ", type (y), '\n')

#stdName is a name of a variable that represents the name of a student.
#stdName is an identifier

stdName = "Yog Chaudhary"

print ("stdName is a variable. It is an identifier. Its value is: ", stdName, "\n")
print("Data type of stdName: ", type (stdName), '\n')


# #### Variable/Identifier stdName:
# 
#  - ***stdName*** is an ***identifier***. It is a ***variable***.
# 
#  - Its ***value*** is "john Smith": "JohN Smith" is ***data***.
# 
#  - The ***variable (identifier)*** stdName is the ***data container*** that contains the piece of data "John Smith".
# 
#  - ***Data*** type of stdName is "str" (or String)
# 
# <font color=red>IMPORTANT NOTES:</font> 
#  - In Python, identifiers are unlimited in length. Case is significant. 
#  - However, the user is strongly discouraged from using a very long name to label variables. Besides, the names should be meaningful.

# ### 3.2 Constants
# Constants are data containers that contain permanent values, i.e., these values cannot be changed, along the course of executing a program.

# In[78]:


#YC95 
# Constaint are often named in uppercase to distinguish the from variables 
max_value = 100
PI = 3.14159
# Pi = 3.14 This will taise an error


# ## 4. Assignments
# ### Overview
# The assignment operator, denoted by the “=” symbol, is the operator that is used to assign values to variables in Python.
# 
# We use Python assignment statements to assign objects to names. The target of an assignment statement is written on the left side of the equal sign (=), and the object on the right can be an arbitrary expression that computes an object. 
#  
# ***Binding a variable*** in Python means setting a name to hold a ***reference*** to some object. 
#   - Assignments create references, not copies.
#  
#  Names in Python do not have an intrinsic type. ***Objects have types***.
#   - Python determines the ***type of the reference*** automatically based on the ***data object*** assigned to it.
#   
#   A name is created when it appears the first time on the left side of an assignment expression:
#   > x = 3
#   
#   A ***reference is deleted*** via garbage collection when NO variables or identifiers refer to it.
#   
# ### 4.1. Reference Semantic in Python
#   
# #### Overview: The process of assigning a value
#   
#   What happens when we type: x = 3?
#   
#    - First, an integer 3 is created and stored in memory
#    - Then a name is created
#    - Next, a reference to the memory location storing the 3 is assigned to the name x
#    
#    
# ### 4.2 Assignment manipulates references
#  - y = x: An assignment of x to y
#  - y = x: The assignment does not make a copy of the value of x.
#  - y = x: The assignment makes y refer to the same object as x does.
#    
# >Let's say you assign x = 3
#  
# >And then you assign y = x  
# 
# When you assign y = x, you now have y = 3 since x = 3 
# 
# Here is an example
# ### <font color=red> **Run the following code:** </font>

# In[27]:


x=3

y=x

y


# <font color=red> **Revise the code block above with xx replacing x and set equal to 12.98, and yy replacing y** </font>

# In[28]:


#YC95
XX = 12.98
YY = XX
YY


# ## 5. Operators and Operations

# ## 5.1 Numeric Operations
# | <font size=4>Operator</font> | <font size=4>Operation</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   | <font size=4>Example</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <font size=4>Result</font> |
# | :--- | :--            | :--     | :-     |
# |<font size=4>+</font>     |<font size=4>Addition</font>        |<font size=4>33 + 3</font>   | <font size=4>36</font>     |
# |<font size=4>- </font>    |<font size=4>Subtraction</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |<font size=4>33 - 3</font>   | <font size=4>30</font>     |
# |<font size=4>* </font>    |<font size=4>Multiplication</font>  |<font size=4>33 * 3</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    | <font size=4>99</font>     |
# |<font size=4>/</font>     |<font size=4>Division</font>        |<font size=4>11 / 3   | <font size=4>3.666  |
# |<font size=4>%</font>     |<font size=4>Remainder</font>       |<font size=4>33 % 3</font>   | <font size=4>0</font>      |
# |<font size=4>**</font>    |<font size=4>Exponent</font>        |<font size=4>33 ** 3</font>  | <font size=4>35937</font>  |
# |<font size=4>// </font>   |<font size=4>Floor</font>           |<font size=4>11 // 3</font>  |<font size=4> 3 </font>     |

# <font color=red> **Insert separate code blocks below to run all the examples above with different randomly selected integers. I am inserting the first line below for an example, you do the rest similarly.** </font>

# In[30]:


# MO54
833 + 21


# In[36]:


#YC95
#Addition 
33+3 


# In[37]:


#YC95
# Subtraction 
33-3


# In[38]:


#YC95
# Subtraction 
55-10


# In[39]:


#YC95
# Multiplication  
33*3


# In[40]:


#YC95
# Multiplication  
100*5


# In[41]:


#YC95
# Division  
11/3


# In[42]:


#YC95
# Division  
78/9


# In[43]:


#YC95
# Remainder
33 % 3


# In[44]:


#YC95
# Remainder
44 % 5


# In[45]:


#YC95
# Expoment 
33 ** 3


# In[46]:


#YC95
# Expoment 
55 ** 5


# ### 5.2 Augmented Operators
# | <font size=4>Operator</font> | <font size=4>Operation</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   | <font size=4>Example</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <font size=4>Result</font> |
# | :--- | :--            | :--     | :-     |
# |<font size=4>+=</font>     |<font size=4>Addition assignment</font>        |<font size=4>i += 8</font>   | <font size=4>i = i + 8</font>     |
# |<font size=4>-= </font>    |<font size=4>Subtraction assignment</font>     |<font size=4>i -= 8</font>   | <font size=4>i = i - 8</font>     |
# |<font size=4>*= </font>    |<font size=4>Multiplication assignment</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |<font size=4>i *= 8</font>   | <font size=4>i = i * 8</font>     |
# |<font size=4>/=</font>     |<font size=4>Division assignment</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         |<font size=4>i /= 8   | <font size=4>i = i / 8  |
# |<font size=4>%=</font>     |<font size=4>Remainder assignment</font>       |<font size=4>i %= 8</font>   | <font size=4>i = i % 8      |
# |<font size=4>**=</font>    |<font size=4>Exponent assignment</font>        |<font size=4>i **= 8</font>  | <font size=4>i = i ** 8</font>  |
# |<font size=4>//= </font>   |<font size=4>Floor assignment</font>           |<font size=4>i //= 8</font>  |<font size=4> i = i // 8 </font>     |

# <font color=red> **Insert separate code blocks below to run all the examples above with different 
# randomly selected integers. I am inserting the first line below for an example, you do the rest similarly.** </font>

# In[50]:


# MO54
i=12
i+=12
i


# In[52]:


# YC95
# Additional assignment 
i=12
i+=12
i


# In[53]:


# YC95
# Subtractin assignment 
i=12
i-=10
i


# In[54]:


# YC95
# Multiplication  assignment 
i=12
i*=10
i


# In[55]:


# YC95
# Division assignment 
i=120
i/=101
i


# In[56]:


# YC95
# Remainder assignment 
i=121
i%=10
i


# In[58]:


# YC95
# Exponebt assignment 
i=11
i**=7
i


# In[59]:


# YC95
# Floor assignment 
i=121
i//=10
i


# ### 5.3 Relational Operators (a.k.a. Comparison Operators)
# 
#  - Relational operators, a.k.a. comparison operators, are used for comparisons.
#  - A comparison, e.g. a>b, is called a conditional expression or boolean expression.
#  - The result of a boolean expression is either True or False.
#  
# |<font size=4>Operator</font>| <font size=4>Meaning</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   | <font size=4>Example</font>     | <font size=4>Ex. Result</font> |
# | :--- | :--            | :----------|  ----:     |
# |<font size=4> (<) </font> |<font size=4>Less than</font>        |<font size=4>radius (<) 0 </font>     | <font size=4>False</font>     |
# |<font size=4>(=<) </font> |<font size=4>Less than or equal to&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </font>  |<font size=4>radius (<=) 0</font>     | <font size=4>True</font>     |
# |<font size=4>(>) </font> |<font size=4>Greater than</font>  |<font size=4>radius (>) 0</font>     | <font size=4>True</font>     |
# |<font size=4>(>=)</font> |<font size=4>Greater than or equal to</font>        |<font size=4>radius (>=) 0     | <font size=4>False </font>  |
# |<font size=4>(==)</font> |<font size=4>Equal to</font>       |<font size=4>radius (==) 0</font>     | <font size=4>True      |
#     |<font size=4>(!=)</font> |<font size=4>Not equal to</font>        |<font size=4>radius (!=) 0</font>    | <font size=4>False</font>  |
# 

# In[ ]:





# <font color=red> **Insert separate code blocks below to run all the examples above after setting the radius to
# a randomly selected number, say 4. I am inserting the first line below for an example, you do the rest 
# similarly.** </font>

# In[65]:


# MO54
radius = 3
radius < 0


# In[67]:


# YC95
radius = 5
radius <=15


# In[69]:


# YC95
radius = 5
radius > 2


# In[71]:


# YC95
radius = 3
radius >= 5


# In[72]:


# YC95
radius = 9
radius == 9


# ### 5.4 Logical Operators
#     
# |<font size=4>Operator</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <font size=4>Meaning</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <font size=4>Example</font> |    
# | :--- |:--------------| :----------| 
# |<font size=4>not</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<font size=4>Opposite</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |<font size=4>not (radius < 0) </font> | 
# |<font size=4>and</font>|<font size=4>And</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       |<font size=4>(a > b) or (c < d)</font>     | 
# |<font size=4>or</font>|<font size=4> Or </font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       |<font size=4>(a > b) or (c < d)</font>    | 

# #### 5.4.2  <font color=blue>and</font> Operators
# a and b ***is true** only when ***both a and b are true***.
#     
# |<font size=4>a</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <font size=4>b</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <font size=4>a <font color=blue>&nbsp;&nbsp;and</font>&nbsp;&nbsp; b </font> |    
# | :--- |:--------------| :----------| 
# |<font size=4>True</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<font size=4>True</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |<font size=4>True </font> | 
# |<font size=4>True</font>|<font size=4>False</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       |<font size=4>False</font>     | 
# |<font size=4>False</font>|<font size=4> True </font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       |<font size=4>False</font>    | 
# |<font size=4>False</font>|<font size=4> False </font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       |<font size=4>False</font>    | 

# ### 5.5 Identity Operators
# In Python, ***identity operators*** are used to check if the ***operands are identical***, i.e., they refer to the same object.
# 
# |<font size=4>Operator</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <font size=4>Result</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <font size=4>Example</font> |    
# | :--- |:--------------| :----------| 
# |<font size=4>is</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<font size=4>True if the operands are identical, i.e., they refer to the same object</font>;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<font size=4>x is y </font> | 
# |<font size=4>is not</font>|<font size=4>True if the operands are not identical, i.e., they do not refer to the same object</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |<font size=4>x is not y </font>     | 
# 

# Let's illustrate what we have learned.
# 
# ### <font color=red> **Run the following 3 code blocks:** </font>

# In[73]:


#YC95
x = 5
y = 5

isTrue = "x is y"
isFalse = "x is not y"

if (x is y):
    print (isTrue)
else:
        print (isFalse)


# In[99]:


#YC95
x = 5
y = 8

isTrue = "x is y"
isFalse = "x is not y"

if (x is y):
    print (isTrue)
    
else:
    print (isFalse)


# In[100]:


#YC95
x = 5
y = 5

isTrue = "x is y"
isFalse = "x is not y"

if (x is not y):
    print (isTrue)
else:
        print (isFalse)


# ### 5.6 Membership Operators
# 
# In Python, many data structures have their internal structure of a sequence, e.g., String, List, Tuple, etc.
# 
# For example:
# 
#  - aString = "Hello World"
# 
#  - aList = [1,2,3,4,5]
# 
#  - aTuple = (1, 2, 3, 4, 5)
# 
# ***Membership operators*** - in, not in - are used to test ***if a value is found*** in a sequence or not.
# 
# |<font size=4>Operator</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <font size=4>Result</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <font size=4>Example</font> |    
# | :--- |:--------------| :----------| 
# |<font size=4>in</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<font size=4>True if the value/variable is found in the sequence</font>;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<font size=4>x in y </font> | 
# |<font size=4>not in </font>|<font size=4>True if the value/variable is not found in the sequence</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |<font size=4>x not in y </font>     | 
# 
# <font color=red> **Run the following 2 code blocks. Never forget to put comments on top of each such code block:** </font>
# 

# In[91]:


#YC95
x = 'Hello World'
if ('H' in x):
    print ("H in x")
else:
        print ("H not in x")


# In[92]:


#YC95
# 
x = 10
y = 10

isTrue = "x is y"
isFalse = "x is not y"

if (x is not y):
    print (isTrue)
else:
        print (isFalse)


# In[98]:


#YC95
# You will get an error but think why you have an error.
aList = [1, 2, 3, 4, 5]
if (8 not isn aList):
    print ("8 not in aList")
else:
    print ("8 in aList")


# ## 6. Pseudo-Code 
# 
# ### Overview
# In machine learning, many developers write pseudo-code for their machine learning algorithms. Python pseudocode is a syntax-free representation of code. So, the Python pseudocode does not involve any code in it. The Python pseudocode is a very close representation of the algorithmic logic. Read through the following scenario to better explain the purpose of pseudo-code.
# 
# ### 6.1 Scenario: A Problem
# 
# It is assumed that a software developer is asked to write a Python program that can calculate and print the diameter and the circumference of a circle. The user enters the data of the radius and its measurement unit (in, ft, cm, or m) from the console.
# 
# ### 6.2 How to Solve the problem
# 
#  - First, we need to write pseudo-code (or create a flow-chart) of steps that can solve the problem. Formally, we design an algorithm that offers a solution to the problem.
#  - Then, based on the steps of the pseudo-code/flowchart (or algorithm), we write the code of the program.
#  
#  These two steps are the foundation of the software engineering process.
#  
# ### 6.3 Pseudo-Code
#  
#  With pseudo-code, the developer writes down the steps to solve the problem in plain English.
#  
#  1. Start
#  2. Read the input of the radius from the console
#  3. Read the measurement unit of the radius (in, ft, cm, m)
#  4. Calculate the diameter of the circle
#      - diameter = 2*radius
#  5. Calculate the circumference of the circle
#      - Circumference = diameter*PI (3.14159)
#  6. Print out the diameter
#  7. Print out the circumference
#  8. End

# <font color=red> **Suppose that you ask a person the year of his/her birth to compute the age of that person.
# Write a pseudo-code for this simple scenario below** </font>

# In[97]:


# The pseudo-code representation of the steps needed developersolve. Here's summary of steps in the pseudo-code: 
1. start. 
2. Read the input of the radiou from the console.
3. Calculation measuremsnt unit of the radiys (in, ft,cm,m).
4. Calculation the daimenter of the circle: diameter = 2 * radius.
5. Calculation the circumferences of the circle: Circumference = diameter * PI (3.14159).
6. Print out the diameter.
7. Print out the circumference.
8 End.
 # Developer can use this pseudo-code as a guide to write the corresponding Python code to implement this algorithm. It 
 # provided a structured approach to solving the problem and can help ensure that the logic is properly translated into code. 


# <font color=green>**Great Job!**<font color=green> 
# 
# <font color=green>**You have learned the fundamentals of programming for data science with Python.**<font color=green>
