#ㅎㅗㅣㅇㅡㅣㅅㅣㄹ ㅇㅖㅇㅑㄱ
n,m = map(int, input().split())
conference = {}

for _ in range(n):
    name = input().rstrip()
    conference[name] = [[i,i+1] for i in range(9,18)]

#print(conference)

for _ in range(m):
    r,s,t = input().split()
    for i in range(int(s),int(t)):
        if [i,i+1] not in conference[r]:
            pass
        else:
            conference[r].remove([i,i+1])
#print(conference)

for value in sorted(conference.keys()):
    if len(conference[value]) == 0: #all-reservation 
        print("Room " + value + ":")
        print("Not available")
        
        if value == sorted(conference.keys())[-1]:
            break
        else:
            print("-----")
    else: #not-all
        print("Room " + value + ":")
        
        temp = [] #check_hours
        answer = [] #save
        for i in range(len(conference[value])):
            #print(i)
            if len(conference[value])==1: #available 1
                temp.append(conference[value][i])
            elif i == len(conference[value]) - 1:
                    temp.append(conference[value][i])
            else: #avilable >= 1
                if conference[value][i][1] == conference[value][i+1][0]: #end=start
                    temp.append(conference[value][i])
                else: #end!=start
                    temp.append(conference[value][i])
                    answer.append([temp[0][0], temp[-1][1]])
                    temp = [] #check_new hours
        #print(temp)
        #print(answer)
        answer.append([temp[0][0], temp[-1][1]])
        #print(answer)
        
        print(len(answer), "available:")
        for idx in answer:
            if idx[0] == 9: idx[0] = '09'
            print(str(idx[0])+'-'+str(idx[1]))
        
        if value == sorted(conference.keys())[-1]:
            break
        else:
            print('-----')
