##CREATED BY : ANISH RAJESH ADNANI
##SEQUENCE ALIGNMENT
##TIME EFFICIENT VERSION
##BASIC LIBRARY IMPORTS
####################################################################################################################
import time
import timeit
from time import process_time
import os, psutil
import sys
#print(type(sys.argv[1]))
pid = os.getpid()
python_process = psutil.Process(pid)
with open(sys.argv[1]) as f:
    contents = f.readlines()
    
process = psutil.Process(os.getpid())
start_time = time.time()
start = process_time()
#####################################################################################################################
##STARTED READING INPUT AND REMOVING \N FROM EACH LINE
for x in range(len(contents)):
    contents[x] = contents[x].strip()##remove all /n from the string ends
#print(contents)

queue1 = []
queue2 = []
indx = 0
####################################################################################################################
## GENERATING WORD1 OPERATIONS
for x in range(1,len(contents)):
    if ord(contents[x][0])<48 or ord(contents[x][0])>57:##find index of second word
        indx = x
        break
        
    else:
        queue1.append(int(contents[x]))


##GENERATING WORD2 OPERATIONS
########################################################################################################################
for x in range(indx+1,len(contents)):##all k values
    queue2.append(int(contents[x]))
        
#print(queue1, queue2)

######################################################################################################################3
##forming the two strings
word1 = contents[0]
word2 = contents[indx]

for x in range(len(queue1)):##forming word1
    temp = word1
    new_word = word1[0:queue1[x]+1] + temp + word1[queue1[x]+1:len(word1)]
    word1 = new_word
    



for x in range(len(queue2)):##forming word1
    temp = word2
    new_word = word2[0:queue2[x]+1] + temp + word2[queue2[x]+1:len(word2)]
    word2 = new_word
    
#print(word1)
#print(word2)
############################################################################################################################
###STARTED BUILDING THE DP ARRAY TIME EFFICIENT MODEL
n1 = len(word1)
n2 = len(word2)

delta = 30
dicts = {}
dicts[('A','A')] = 0
dicts[('A','C')] = 110
dicts[('A','G')] = 48
dicts[('A','T')]  = 94

dicts[('C','C')] = 0
dicts[('C','A')] = 110
dicts[('C','G')] = 118
dicts[('C','T')] = 48

dicts[('G','G')] = 0
dicts[('G','A')] = 48
dicts[('G','C')] = 118
dicts[('G','T')] = 110

dicts[('T','T')] = 0
dicts[('T','A')] = 94
dicts[('T','C')] = 48
dicts[('T','G')] = 110
#print(dicts)
#print(('C', 'C') in dicts)
dp = [[0 for x in range(n1+1)]for y in range(n2+1)]

for x in range(1,n1+1):
    dp[0][x] = x*delta
    

for x in range(1,n2+1):
    dp[x][0] = x*delta
    
for x in range(1,n2+1):
    for y in range(1,n1+1):
        temp = word1[y-1]
        temp2 = word2[x-1]
        key = (temp,temp2)
        dp[x][y] = min(dp[x-1][y-1]+dicts[key],dp[x-1][y]+delta,dp[x][y-1]+delta)
        
#print("word on row is",word1)
#print("word on col is",word2)
#for x in range(len(dp)):
    #print(dp[x])
    
#print("total allignment cost is",dp[n2][n1])

seq1 = []
seq2 = []
#########################################################################################################3
##STARTED TOP DOWN TRAVERSAL ON DP ARRAY TO GET ALLIGNMENTS
counter1 = n2
counter2 = n1
while (counter1!=0 and counter2!=0):
    #print(counter1,counter2)
    temp1 = word1[counter2-1]
    temp2 = word2[counter1 - 1]
    
    keys = (temp1,temp2)
    #print(counter1,counter2,temp1,temp2,keys)
    if dp[counter1][counter2] == dp[counter1-1][counter2-1] + dicts[keys]:
        seq1.append(temp1)
        seq2.append(temp2)
        counter1-=1
        counter2-=1
    elif dp[counter1][counter2] == dp[counter1-1][counter2] + delta:
        seq1.append("_")
        seq2.append(temp2)
        counter1-=1
        
    elif dp[counter1][counter2] == dp[counter1][counter2-1] + delta:
        seq1.append(temp1)
        seq2.append("_")
        counter2-=1
    

while counter1!=0:
    temp2 = word2[counter1 - 1]
    seq1.append("_")
    seq2.append(temp2)
    counter1-=1
    
while counter2!=0:
    temp1 = word1[counter2 - 1]
    seq1.append(temp1)
    seq2.append("_")
    counter2-=1
#print("Final alignments are as follows")
end_time = time.time()
end = process_time()
seq1=seq1[::-1]
seq2=seq2[::-1]
memoryUse = python_process.memory_info()[0]/2.**30
#print(seq1)
#print(seq2)
#print(end_time - start_time)
#print((process.memory_info().rss)*0.000001*1024, "KB") 
##################################################################################################################################################################      
##STARTED PREPARING THE OUTPUT FILE

outputfile = open("output.txt","w")
startw1 = ""
endw1 = ""
startw2 = ""
endw2 = ""
for x in range(50):
    startw1+=seq1[x]
    startw2+=seq2[x]
    endw1+=seq1[len(seq1)-50+x]
    endw2+=seq2[len(seq2)-50+x]


outputfile.write(startw1+" "+endw1+"\n")
outputfile.write(startw2+" "+endw2+"\n")
outputfile.write(str(float(dp[n2][n1]))+"\n")
outputfile.write(str(float(end_time- start_time))+"\n")
outputfile.write(str((process.memory_info().rss)*0.000001*1024))

outputfile.close()

#print("Your output file named output.txt is created")
#print(seq1,seq2)   
 
 
 
 
 
