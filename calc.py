#split string ( ',' && '\n' )and convert it into number and return list of number 
def split(str):
    arr=[]
    narr=[]
    num=""
    try :
        for ch in str:
            if (ch==',' or ch== '\n'):
                if (int(num)>=0 and int(num)<=1000):
                    arr.append(int(num))
                elif (int(num)<0) :
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


def splitAny(str,delimiter, k):
    arr=[]
    num=""
    try :
        # print(delimiter)
        flag=False
        for i in range (k,len(str)):
            if (str[i]<'0' or str[i]>'9') :  
                if flag :
                    arr.append(int(num))
                num=""
                flag=False

            else :
                flag=True
                num = num + str[i]
        arr.append(int(num))
    except :
        print("splitAny :- Unexpected String or delimiters")
    
    return arr 



def add(str):
    try :
        arr= []
        if(len(str)==0) :
            return 0
        
        if str[0] != '/' :
            arr = split(str) 
        elif(str[0]=='/' and str[1]=='/'):
            if(str[3]=='\n'):
                arr = splitByAnyCharacter(str,str[2])
            elif (str[2]=='['):
                k=3
                delimiter = []        # store all delimiter
                while(str[k]!='\n'):
                    s=""
                    while(str[k]!=']'):
                        s= s + str[k]
                        k= k+1 
                    k= k+1 
                    delimiter.append(s)
                arr = splitAny(str,delimiter,k+1)


                


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

    #Numbers bigger than 1000 should be ignored
    add("1,2,1001,5")

    # Delimiters can be of any length
    add("//[***]\n1***2***3")

    # Allow multiple delimiters
    add("//[*][%]\n1*2%3")

    # multiple delimiters with length longer than one char
    add("//[*][%%]\n1*5%%3")


test()
