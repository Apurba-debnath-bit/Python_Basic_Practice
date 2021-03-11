import sys as sd
print(sd.path)

#only import keyword used . mendartory.
import file2
print(file2.a)

#more specific: using from keyword import what
from file2 import a
print(a)

#which is better :
import file2
file2.a

#embiguous problem:
#suppose file2 has a and file3 both has a then what will do python:
#file.a is a solution for ambiguty

print("function calling from another file:....")
import file2
file2.joke("love you baby!!")

#Never used any python file's name as any python module's name.

