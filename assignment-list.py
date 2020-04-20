'''
name, regno,sub1,sub2
who has scrored highest in each subject and in total
'''
markslist = []
titlelist = ["name","regno","sub1","sub2"]
markslist.append(titlelist)
datastud1 = ["raghu",100,78,89]
datastud2 = ["lokesh",101,88,81]
datastud3 = ["vidya",102,98,83]
markslist.append(datastud1)
markslist.append(datastud2)
markslist.append(datastud3)
print('marks list ',markslist)
sub1max = 0
sub2max = 0
totalmax = 0
aboveeighty = 0

sub1maxindex = 0
sub2maxindex = 0
totalmaxindex = 0
  
for i in range(1,len(markslist)):
    print(markslist[i])
    studmarks = markslist[i]
    sub1marks = studmarks[2]
    sub2marks = studmarks[3]
    name = studmarks[0]
    totalmarks = sub1marks+sub2marks
    
    if (sub1marks > sub1max):
        sub1max = sub1marks
        sub1maxindex = i
        
    if (sub2marks > sub2max):
        sub2max = sub2marks
        sub2maxindex = i
        
    if (totalmarks > totalmax):
        totalmax = totalmarks
        totalmaxindex = i
        
    if (sub1marks > 80):
        aboveeighty=i
        print(markslist[aboveeighty])

    
print('maximum marks for subject 1 ',sub1max)
print('maximum marks for subject 2 ',sub2max)
print('topper (sub1 and sub2) ',totalmax)
print('maximum marks scorer for subject 1 ',markslist[sub1maxindex])
print('maximum marks scorer for subject 2 ',markslist[sub2maxindex])
print('maximum marks scorer for both sub1 and subject 2 ',markslist[totalmaxindex])

'''
dynamic list
'''

'''
name, regno,sub1,sub2
who has scrored highest in each subject and in total
'''
markslist = []
titlelist = ["name","regno","sub1","sub2"]
markslist.append(titlelist)
noofstud = int(input("Enter no of students"))

for i in range (noofstud):
    name = input ("Enter name")
    regno = int(input ("Enter reg no"))
    sub1 = int(input ("Enter subject1 marks"))
    sub2 = int(input ("Enter subject2 marks"))
    studlist = [name,regno,sub1,sub2]
    markslist.append(studlist)
    
print('marks list ',markslist)
'''
datastud1 = ["raghu",100,78,89]
datastud2 = ["lokesh",101,88,81]
datastud3 = ["vidya",102,98,83]
markslist.append(datastud1)
markslist.append(datastud2)
markslist.append(datastud3)
print('marks list ',markslist)
'''
sub1max = 0
sub2max = 0
totalmax = 0
aboveeighty = 0

sub1maxindex = 0
sub2maxindex = 0
totalmaxindex = 0
  
for i in range(1,len(markslist)):
    print(markslist[i])
    studmarks = markslist[i]
    sub1marks = studmarks[2]
    sub2marks = studmarks[3]
    name = studmarks[0]
    totalmarks = sub1marks+sub2marks
    
    if (sub1marks > sub1max):
        sub1max = sub1marks
        sub1maxindex = i
        
    if (sub2marks > sub2max):
        sub2max = sub2marks
        sub2maxindex = i
        
    if (totalmarks > totalmax):
        totalmax = totalmarks
        totalmaxindex = i
        
    if (sub1marks > 80):
        aboveeighty=i
        print(markslist[aboveeighty])

    
print('maximum marks for subject 1 ',sub1max)
print('maximum marks for subject 2 ',sub2max)
print('topper (sub1 and sub2) ',totalmax)
print('maximum marks scorer for subject 1 ',markslist[sub1maxindex])
print('maximum marks scorer for subject 2 ',markslist[sub2maxindex])
print('maximum marks scorer for both sub1 and subject 2 ',markslist[totalmaxindex])

'''
ipl match
'''
statlist = []
titlelist = ["name","team","season","matches","runs","wickets"]
statlist.append(titlelist)
dataplay1 = ["virat","rcb",2019,18,897,0]
dataplay2 = ["abd","rcb",2019,14,765,0]
dataplay3 = ["jadeja","csk",2019,17,688,12]
dataplay4 = ["pollard","mi",2019,16,700,13]            
statlist.append(dataplay1)
statlist.append(dataplay2)
statlist.append(dataplay3)
statlist.append(dataplay4)
print("stat list",statlist)
runsmax=0
wicketsmax=0             

runsmaxindex=0
wicketsmaxindex=0

for i in range(1,len(statlist)):
    print(statlist[i])
    playstat= statlist[i]
    runsstat= playstat[4]
    wicketsstat=playstat[5]
    name = playstat[0]

    if(runsstat>runsmax):
       runsmax = runsstat
       runsmaxindex=i

    if(wicketsstat>wicketsmax):
       wicketsmax= wicketsstat
       wicketsmaxindex=i

print('maximum runs scorer ',runsmax)
print('maximum runs scorer details ',statlist[runsmaxindex])

print('maximum wicketsfor taker ',wicketsmax)
print('maximum wicketsfor taker info ',statlist[wicketsmaxindex])



'''
name,team,runs,wickets
who has scrored hbighest runs in each match and in total
'''
playerlist= []
titlelist = ["name","team""runs","wickets"]
playerlist.append(titlelist)
dataplayer1 = ["virat","RCB",897,0]
dataplayer2 = ["ABD","RCB",765,0]
dataplayer3 = ["JADEJA","CSK",688,12]
dataplayer4 = ["POLLARD","MI",700,13]
playerlist.append(dataplayer1)
playerlist.append(dataplayer2)
playerlist.append(dataplayer3)
playerlist.append(dataplayer4)
print('player list ',playerlist)
runsmax=0
wicketsmax=0
runsmaxindex=0
wicketmaxindex=0
for i in range(1,len(playerlist)):
    print(playerlist[i])
    playerstat = playerlist[i]
    runs = playerstat[2]
    wickets = playerstat[3]
   
    if (runs > runsmax):
        runsmax = runs
        runsmaxindex=i
    
    if(wickets>wicketsmax):
        wicketsmax=wickets
        wicketsmaxindx=i
print('maximum runs scorer  for runsmax ',runsmax)
print('maximum wickets taken for wicketsmax',wicketsmax)
             














    