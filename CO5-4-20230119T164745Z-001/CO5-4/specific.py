import csv

#specify the column indices that you want to read
#e.g. column 0 is the first column 1 is the second column, etc.
columns_to_read = [0,2]

#open the csv file and read the contents
with open('spxl.csv','r') as file:
    clmn_reader = csv.reader(file)

    # iterate over the rows of the CSV file
    for row in clmn_reader:
        # Print the contents of the specifed columns
         print([row[i] for i in columns_to_read])