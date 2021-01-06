import csv
import sys

# infile is a csv file that includes a colum called "username"
# The gender is identified by checking the username with the names in the census dataset
# The file "quantified_gender_1900_2013.txt" includes all names used between 1900 to 2013, and
# For each name, it also shows the probability that a name is female and male
# outfile is in csv format. It has one additional column compared to infile which is called gender.
#


infile_name = sys.argv[1]
outfile_name = sys.argv[2]

with open(infile_name) as infile, open(outfile_name, "w", newline="") as outfile:
    r = csv.DictReader((line.replace('\0','') for line in infile), delimiter=",")
    fieldnames = r.fieldnames + ['gender'] 
    w = csv.DictWriter(outfile, fieldnames, extrasaction="ignore")
    w.writeheader()

    #gender
    qfile = open('quantified_gender_1900_2013.txt', encoding='cp437')
    lines = qfile.read().splitlines()
    qnames = {}
    for line in lines:
        words = line.split(' ')
        #print(words[0] + " " + words[1])
        qnames[words[0]] = words[1] 
    qfile.close()

# N: no firstname found
# M: Male
# N: Female
# A: ambiguous

    i =0
    for row in r:
        # quantfied_gender
        name = row["username"]
        row["gender"] = "N"
        #check first name
        if name.isalpha():
            firstname= name.strip().lower()
            if firstname in qnames.keys():
                gen = qnames[firstname]
                if float(gen) >= 0.95: 
                    row["gender"] = "M"
                elif float(gen) <= 0.05: 
                    row["gender"] = "F" 
                else:
                    row["gender"] = "A" 

        w.writerow(row)
        #print(str(i))
        i = i + 1

    print(i)
