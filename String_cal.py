def test():
    #empty string
    assert(add("")==0)
    
    #1 Number
    assert(add("1")==1)
    assert(add("2")==2)
    
    #2 numbers
    assert(add("1,2")==3)
    assert(add("a,2")== 3)
    assert(add("5,3000")==5)
    
    #3 numbers
    assert(add("1,2,3")==6)
    assert(add("2,3,6")==11)
    
    #New Lines
    assert(add("1\n2")==3)
    assert(add("3\n4")==7)
    
    #Handle Different Delimiters
    assert(add("//;\n1;2;3")==6)
    assert(add("//-\n1-2-3")==6)
  
    
    print("Passed all tests")
    
def add(numbersString):
    if len(numbersString)==0:
        return 0
    elif len(numbersString)==1:
        return int(numbersString)
    elif numbersString[0]=="/":
        result=0
        delim=numbersString[2]
        numbers=numbersString.split("\n")[1].split(delim)
        return multipleNumbers(numbers)
    
    else:
        result=0
        delim=","
        if numbersString[1] != ",":
            delim="\n"
        numbers= numbersString.split(delim)
        # for num in numbers:
        #     result += int(num)
        return multipleNumbers(numbers)
    
def multipleNumbers(numbers):
    result=0
    #numbers=numbersString.split(delim)
    for num in numbers:
        if(num.isalpha()):
            num=ord(num)-96
        
        elif(int(num)>1000):
            num="0"
        result+=int(num)
        

        
    return result 
    
test()
