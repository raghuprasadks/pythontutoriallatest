'''
Mode	Description
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
'''
def main():
    f= open("dhanyatest12.txt","w+")
    print('w+ mode')
    for i in range(1,30):
        #print(i)
        f.write("This is new line %d\r\n" % (i))      
    f.close()
    try:
    #Open the file back and read the contents
        f=open("dhanyatest12.txt", "r")
        f.seek(0,0)
    #if(f.mode == 'r'):
        print('reading')
        contents =f.read()
        print(contents)
    except Exception as e:
        print('exception',e)
   #or, readlines reads the individual line into a list
   #fl =f.readlines()
   #for x in fl:
   #print x
    f.close()
    
if __name__== "__main__":
  main()
  
#Open a file in append mode.
f= open("aprilcoronapython.txt","w")
#print(f)    
f.write('I am learning python\n')
f.write('python is easy to learn\n')
f.close()
 
#file in append mode.
f= open("aprilcoronapython.txt","a")    
f.write('Month of Corona..\n')
f.write('Not allowing us to do hindi corona..\n')
f.write("Using write mode \n")
f.close()

#Reading a file r mode.
f= open("aprilcoronapython.txt","r")    
print(f.read())
f.close()

#Reading line by line
f= open("aprilcoronapython.txt","r")    
lines = f.readlines()
for l in lines:
    print(l)
f.close()

#Sum of numbers in a file
f= open("samplefile.txt","r")    
lines = f.readlines()
tokens = ''
sum = 0
for l in lines:
    tokens = l.split()
    for token in tokens:
        if (token.isnumeric()):
            sum = sum + int(token)
            print(token) 
print('sum : ',sum)
f.close()

#https://www.tutorialsteacher.com/python/python-read-write-file
f= open("dhanyatest12.txt","a+")
f.write('testing')
f.seek(10,0)
contents =f.read()
print(contents)
print(f.mode)
f.close()

f=open("binfile.bin","w+b")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.seek(0,0)
print(list(f.read()))
f.close()


f=open("binfile.bin","w+b")
num=['r', 'a']
arr=bytearray(str(num),'utf-8')
f.write(arr)
f.seek(0,0)
print((f.read().decode()))
f.close()

string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)


with open('testfile.txt', 'r') as reader:
    # Read & print the entire file
    print(reader.read())

'''
CSV files
'''

#import necessary modules
import csv

with open('writeData.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #way to write to csv file
    writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])



#import necessary modules
import csv
with open('writeData.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)
        
#import necessary modules
import csv

reader = csv.DictReader(open("writeData.csv"))
for raw in reader:
    print(raw)
    
#https://www.geeksforgeeks.org/working-csv-files-python/
    
    
class Customer():
    
    def __init__(self,name,mobile,email,address,city,zipcode):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.address = address
        self.city = city
        self.zipcode = zipcode
    
    def info(self):
        return "Customer: name ",self.name,"Address:  ",self.address




customerList = []
c1 = Customer('raghu',9845547471,'prasadraghuks@gmail.com','1094,MCECHS Layout','Bengaluru',560077)
customerList.append(c1)

c2 = Customer('rudresh',9845547472,'prasadrudreshks@gmail.com','1095,MCECHS Layout','Bengaluru',560077)
customerList.append(c2)

c3 = Customer('girish',9845547473,'girish@gmail.com','1096,MCECHS Layout','Bengaluru',560077)
customerList.append(c3)

'''
create csv
'''
import csv

with open('customerData1.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    headerdata=["name","mobile","email","address","city","zipcode"]
    
    writer.writerow(headerdata)
    for c in customerList:
        data=[]
        data.append(c.name)
        data.append(c.mobile)
        data.append(c.email)
        data.append(c.address)
        data.append(c.city)
        data.append(c.zipcode)
        writer.writerow(data)


import csv
with open('customerData1.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row[0],row[1],row[2])
        
'''
ipl
'''        
        
class IPL():

    def __init__(self, name, team, season, runs, wickets):
        self.name = name
        self.team = team
        self.season = season
        self.runs = runs
        self.wickets = wickets

    def info(self):
        return 'Name : ', self.name, 'Team : ', self.team, 'Season : ', self.season, 'Runs : ', self.runs, 'Wickets : ', self.wickets


ipllist = []
i1 = IPL('virat', 'rcb', 2019, 1200, 0)
ipllist.append(i1)
i2 = IPL('abd', 'rcb', 2019, 1000, 0)
ipllist.append(i2)
i3 = IPL('jadeja', 'csk', 2019, 800, 10)
ipllist.append(i3)
i4 = IPL('bumrah', 'mi', 2019, 120, 15)
ipllist.append(i4)
i5 = IPL('virat', 'rcb', 2018, 12000, 0)
ipllist.append(i5)
i6 = IPL('abd', 'rcb', 2018, 20000, 0)
ipllist.append(i6)
i7= IPL('jadeja', 'csk', 2018, 1800, 110)
ipllist.append(i7)
i8 = IPL('bumrah', 'mi', 2018, 1020, 105)
ipllist.append(i8)

'''
create csv
'''
import csv
totalruns = 0
totalwickets = 0
with open('ipldata.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    headerdata=["name","team","season","runs","wickets"]
    
    writer.writerow(headerdata)
    for i in ipllist:
        data=[]
        data.append(i.name)
        data.append(i.team)
        data.append(i.season)
        data.append(i.runs)
        data.append(i.wickets)
        writer.writerow(data)
        totalruns = totalruns +i.runs
        totalwickets = totalwickets +i.wickets
    footerdata=["Total","","",totalruns,totalwickets]
    writer.writerow(footerdata)

