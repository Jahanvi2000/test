 
from audioop import avg
from html.entities import name2codepoint
import re
from tkinter.ttk import Separator
def string_calc(string):
    if re.match('-[0-9]+',string):
        raise ValueError("negative not allowed {} ".format(re.findall('-[0-9]+',string)))
        separators = ',','\\n'
        if "//" in string:
            sep_info = re.findall('//.+\n',string)[0]
            Separator = sep_info.replace('//','').replace('\\n','')
            string = string.replace(sep_info,'')
        if not string:
            return 0
        if not any(separator in string for separator in separators):
            return int(string)

            return sum(int(number)for number in re.split('|'.join(seoarators),string))
#2             
def avgfun(*n):
    sums=0
    for t in n:
        sums = sums + t
        return sum
result = avgfun(1,2)
result1 = avgfun(1,2,3)
print(round(result,2))
print(round(result1,3))

#3
l1 = [1,2,3,4]
l2 =['a','b','c','d']
l3 = l1+l2
print(l3)
#4
try:
    i = int(input("enter positive num"))
if i <=0:
    raise ValueError ("this is not positive numbers")
    except  ValueError as e:
    print(e)    
#5   
try:
    ch = int(input("enter num"))
    assert ch>0
    except AssertionError:
    print("number is negative")
#6
num1 = 10000
print(f"{num1:,}")  
#7
inpu = raw_inout("entr ints\n").split(',')
inpu = [c.strip() for c in inpu]
print ("\n".inpu)      

   
   
