# Program to copy oddlines of one file to another
#opening files for reading and writing data
input_file = open('Data.txt')
output_file = open('writeData.txt','w')

#copying/reading contents from read_file to copy_data
copy_data =input_file.readlines()
print("\n Actual file is:")
print(copy_data, "\n")

for i in range(0,len(copy_data)):
    if i % 2 == 0 :
        output_file.write(copy_data[i])
    else:
        pass
#closing file after writting
output_file .close()

#opening write file in read mode and printing values
output_file = open ('WriteData.txt','r')
print("\n Odd lines are")
print(output_file.read)

#closing files
input_file.close()
output_file.close()