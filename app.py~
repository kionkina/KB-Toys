"""Karina Ionkina, Ibnul Jahan
SoftDev1 pd7
HW05 -- Jinja Tuning
2017-09-26
"""

import random
#'r' -- read mode: file is only being read.
#file object is created
file = open("occupations.csv", 'r')

#.read() extracts a string that contains all characters in the file
#print file.read()
"""
.readline(): read a file line by line
print file.readline() 

#.readlines() returns array with separate lines
print file.readlines()
"""

#initialize empty dictionary
d = {}

#file.readlines is an array with the lines of the documents
#we parse starting at index 1
for str in file.readlines()[1:len(file.readlines())-1]:
    line = str.split(',')
    #if there are commas in the job class
    if len(line) > 2:
        the_key = ",".join(line[:len(line)-1])
        d[the_key] = float(line[len(line) - 1])
    else:
        d[line[0]] = float(line[1])
#print d

def rand_job():
	count = 0
	#count represents the running total of the for loop through the dictionary
	rand = random.randint(1,998)
	#rand represents a random number between 1 and 998, which coincides with the values of the percentages of the jobs
	#print rand
	for key in d:
		count = count + (d[key]*10)
		#add to count to find out which occupation to stop at
		#print count
		if count >= rand:
			#when your count surpasses the random number, you are in the percentage of that occupation
			return key





from flask import Flask, render_template
app = Flask(__name__) #create instance of class 

#assign following fxn to run when
#root route requested

@app.route("/")
def ret():
    title = "Homework 05"
    return  render_template('speed.html', the_title = title, occupation = rand_job(),  collection = d)

if __name__=="__main__":
    app.debug = True
    app.run()

