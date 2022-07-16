#split string ( ',' && '\n' )and convert it into number and return list of number 
def split(str):
    arr=[]
    narr=[]
    num=""
    try :
        for ch in str:
            if (ch==',' or ch== '\n'):
                if (int(num)>=0):
                    arr.append(int(num))
                else :
                    narr.append(int(num))
                num=""
            else :
                num = num + ch 
        if (int(num)>=0):
            arr.append(int(num))
        else :
            narr.append(int(num))
    except :
        print("Unexpected String")

    if(len(narr)>0) :
        print ("negative is not allowed" , end=": ")
        print(narr)
    return arr 


# Split string by any delimiter and store numbers in array 
def splitByAnyCharacter(str,c) :
    arr=[]
    num=""
    try :
        for i in range (4,len(str)):
            if (str[i]==c):
                arr.append(int(num))
                num=""
            else :
                num = num + str[i]
        arr.append(int(num))
    except :
        print("Unexpected String or delimiters")
    
    return arr 




def add(str):
    try :
        arr= []
        if(len(str)==0) :
            return 0
        
        if str[0] != '/' :
            arr = split(str) 
        elif(str[0]=='/'):
            arr = splitByAnyCharacter(str,str[2])


        sm=0
        for x in arr :
            sm += x 

        print(sm)

    except :
        print("Error!! ")


def test():
    # empty string
    add("")

    #1 or 2 Numbers
    add("4")
    add("1,23")

    #unknow amount of numbers
    add("1,23,34,54")
    add("5,4,3\n10,11\n12")

    #any delimiters
    add("//;\n1;2")
    add("//#\n11#25#46#4")
    #negative number
    add("1,-23,34,54")


test()
