#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

features_dict = {}

for col in range(0,14):
    features_dict[col]=[]
           
# if os.path.isfile(myfilename):
#   print("yay, I have a file")
#   if sky == blue:
#     print('yay the sky is blue')
# else:
#   print ('boo, no files for me')

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        #print(values)
        list=[]   
        i=0
        for value in values:
            # for homework:
            # identify what type of data each value is, and cast it
            # to the appropriate type, then print the new, properly-typed
            # list to the screen.
            # I.e. ['0.04741', '0.00', '11.930', '0', '0.5730', '6.0300', '80.80', '2.5050', '1', '273.0', '21.00', '396.90', '7.88', '11.90']
            # becomes: [0.04741, 0.0, 11.93, 0, 0.573, '6.03, 80.8, 2.505, 1, 273.0, 21.0, 396.90, 7.88, 11.90]                         
            int_list = [3,8]
            two_decimal_positions = [11,13]
            
            if (i in int_list):
                list.append(int(value))
            
            elif (i in two_decimal_positions):
                #here i tried multiple stuff to keep the second decimal zero like in 11.90 whithout having the whole thing as a string, unfortunately it did not work for me
                #list.append("{0:.2f}".format(float(value)))
                #list.append('%.2f' % float(value))
                #list.append(float(format(float(value), '.2f')))
                list.append(round(float(value),2))                
            
            else: list.append(float(value))
                        
            i +=1                    

        print (list)
        
        #new list (here i used a dictionary) for each of the columns in the dataset
        for col in range(0,14):
            features_dict[col].append(list[col])

    print ("\n**Print Features Columns Data**\n")
    for  col in range(0,14):
        print (features_dict[col])

    print('finished!')
    
