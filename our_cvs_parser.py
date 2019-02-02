#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

if os.path.isfile(myfilename):
   print("yay i have a file")
else:
   print ('boo i dnt have a file')

with open(myfilename, 'r') as file_handle: #the adv is that it does the close for us
   #line = file_handle.readline()
   for line in file_handle.readlines():
      #print (line)
      line_clean = line.replace('   ',' ').replace('  ',' ')
      line_clean = line_clean.strip()
      values = (line_clean.split(' ')) #split on this character and put in a list
      print (values)
      for value in values:
         print float(value)

#file_handle = open(myfilename, 'r')
#do something
#file_handle.close()
