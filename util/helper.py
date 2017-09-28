"""Karina Ionkina, Ibnul Jahan
SoftDev1 pd7
HW05 -- Jinja Tuning
2017-09-26
"""
import random  
 
def csv_to_dict(file):
    d = {}
    for str in file.readlines()[1:len(file.readlines())-1]:
        line = str.split(',')
        #if there are commas in the job class
        if len(line) > 3:
            the_key = ",".join(line[:len(line) - 2])
            d[the_key] = ",".join(line[len(line) - 2:])
        else:
            d[line[0]] = ",".join(line[1:])
    return d


def rand_job(d):
	count = 0
	#count represents the running total of the for loop through the dictionary
	rand = random.randint(1,998)
	#rand represents a random number between 1 and 998, which coincides with the values of the percentages of the jobs
	#print rand
	for key in d:
		count = count + (float(d[key].split(',')[0])*10)
		#add to count to find out which occupation to stop at
		#print count
		if count >= rand:
			#when your count surpasses the random number, you are in the percentage of that occupation
			return key


