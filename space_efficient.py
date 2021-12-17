##CREATED BY : ANISH RAJESH ADNANI
##SEQUENCE ALIGNMENT
##SPACE EFFICIENT VERSION
##################################################
##BASIC IMPORT FILES
import time
import timeit
from time import process_time
import os, psutil
import sys
pid = os.getpid()
python_process = psutil.Process(pid)
#with open('input.txt') as f:
with open(sys.argv[1]) as f:
    contents = f.readlines()
    
process = psutil.Process(os.getpid())
start_time = time.time()

########################################################
##STARTED READING INPUT AND REMOVING \N FROM EACH LINE
for x in range(len(contents)):
    contents[x] = contents[x].strip()##remove all /n from the string ends
#print(contents)

##################################################
##GENERATING WORD1 OPERATIONS
queue1 = []
queue2 = []
indx = 0
for x in range(1,len(contents)):
    if ord(contents[x][0])<48 or ord(contents[x][0])>57:##find index of second word
        indx = x
        break
        
    else:
        queue1.append(int(contents[x]))
#for x in range(1,indx):##all j values
    #queue1.append(int(contents[x]))
    
for x in range(indx+1,len(contents)):##all k values
    queue2.append(int(contents[x]))
        
#print(queue1, queue2)

####################################################
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
#print("_____started space eff soln___________")
#################################################
##Used to find where to split y for mid of x
##Used to find where to split y for mid of x
def find_split_y(word1,word2):

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

    dp = [[0 for x in range(n1+1)]for y in range(n2+1)]
    a1 = [x*delta for x in range(n1+1)]
    a2 = [0 for x in range(n1+1)]
    
    ans = []
    ans.append(delta*(n1))
    
    for x in range(1,n2+1):
        a2[0] = x*delta
        for y in range(1,n1+1):
            temp1 = word1[y-1]
            temp2 = word2[x-1]
            key = (temp1,temp2)
            a2[y] = min(a1[y-1]+dicts[key],a1[y]+delta,a2[y-1]+delta)
        #print(a1,a2)   
        a1 = []
        a1 = a2
        ans.append(a2[len(a2)-1])
        a2 = [0 for x in range(n1+1)]
        
        
    
    return ans

###########################################################################
##Dividing the sequence and solving the base case
delta = 30
def space_eff_dp(word1,word2):
    aligned_a = []
    aligned_b = []
    cost = 0
    #print(cost)
    #print("hello",word1,word2)
    if len(word1) == 0:
        for x in range(len(word2)):
            aligned_a.append("_")
            aligned_b.append(word2[x])
            cost = delta * len(word2) ##initial mistake cost+= delta*len(word2)
            
    elif len(word2) == 0:
        for x in range(len(word1)):
            aligned_a.append(word1[x])
            aligned_b.append("_")
            cost =delta*len(word1)
            
    elif len(word1) == 1:
        seq1,seq2,costs = align_this(word1,word2)
        #print("hi",costs)
        for x in range(len(seq1)):
            aligned_a.append(seq1[x])
            aligned_b.append(seq2[x])
        cost = costs
            #cost+=costs
        
    else: 
        mid = len(word1) // 2

        new_word1 = word1[mid:len(word1)]
        new_word1 = new_word1[::-1]
        a = find_split_y(word1[0:mid],word2)
        b = find_split_y(new_word1,word2[::-1])
        b = b[::-1]
        ans = [0 for x in range(len(a))]
        for x in range(len(a)):
            ans[x] = a[x]+b[x]

        split_point = ans.index(min(ans))
        #print("Split point is ",split_point)
        aligned_a_left,aligned_b_left,cost1 = space_eff_dp(word1[0:mid],word2[0:split_point])
        aligned_a_right, aligned_b_right,cost2 = space_eff_dp(word1[mid:len(word1)],word2[split_point:len(word2)])
        
        aligned_a = aligned_a_left + aligned_a_right
        aligned_b = aligned_b_left + aligned_b_right
        cost+= cost1+cost2
        
    return aligned_a,aligned_b,cost
        
        

###################################################################################
##this is the base alignment function
def align_this(word1,word2):

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

    ##backtracking starts here
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
    seq1=seq1[::-1]
    seq2=seq2[::-1]
    #print(seq1)
    #print(seq2)
    return seq1, seq2, dp[n2][n1]
    
        
#####################################
######################################
temp = space_eff_dp(word1,word2)

memoryUse = python_process.memory_info()[0]/2.**30
#print(temp,end_time-start_time)
########################################################
##STARTED PREPARING OUTPUT FILE
outputfile = open("output.txt","w")
end_time = time.time()
startw1 = ""
endw1 = ""
startw2 = ""
endw2 = ""
for x in range(50):
    startw1+=temp[0][x]
    startw2+=temp[1][x]
    endw1+=temp[0][len(temp[0])-50+x]
    endw2+=temp[1][len(temp[1])-50+x]
    
outputfile.write(startw1+" "+endw1+"\n")
outputfile.write(startw2+" "+endw2+"\n")
outputfile.write(str(float(temp[2]))+"\n")
outputfile.write(str(float(end_time- start_time))+"\n")
outputfile.write(str((process.memory_info().rss)*0.000001*1024))
#outputfile.write(str((process.memory_info().rss / 1024 ** 2) * 1000))

outputfile.close()

#print("Your output file named output.txt is created")




