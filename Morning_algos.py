#“ String: Is Palindrome
#Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", return true. Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.”

#Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.  

1. 

def palindrome (stringInput):
    newstring = ""
    for i in range(len(stringInput)-1, -1, -1):
        newstring += stringInput[i]
    if newstring != stringInput:
        return (False)
    elif newstring == stringInput:
        return (True)
    return newstring
print(palindrome('tacocat'))

2.

def pal(stringInput):
    # leftside = stringInput[0]
    # rightside = stringInput[len(stringInput)-1]
    for i in range(0, len(stringInput)//2, 1):
        if stringInput[i] != stringInput[len(stringInput)-1-i]:
            return False

    return True


print(pal("aabyllybaa"))

3.

def reverseString(stringInput):
    # code for the reverse string function
    newstr = ""
    for i in range(len(stringInput)-1, -1, -1):
        newstr += stringInput[i]

    return newstr




def isPalindrome(stringInput):
    #find the reverse of the original string and compare it
    result = reverseString(stringInput)
    if result != stringInput:
        return False
    else:
        return True

print(isPalindrome("racecarlkj"))


“ Acronyms
#Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given " there's no free lunch  -  gotta pay yer way. ", return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN”

#Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.

def acronymGenerator(stringInput):
    # 1. create a new string to put acronym into
    # 2. the first letter of the input string, put it into the new string 
    # 3. go through each character in the string, and when i find a space character-> then put the character that comes after the space into the new string- > do this till we get to the end of the original string
    # 4. return this new string
    pass


def acronym(data):
    acro = ""
    for x in range(0, len(data), 1):
        if x == 0:
            acro+=(data[x])
        elif data[x] == " ":
            acro+=(data[x+1])
    return acro.upper()

print(acronym("national basketball association"))


def acronymGenerator(stringInput):
    # 1. create a new string to put acronym into
    newstring = ""
    # 2. the first letter of the input string, put it into the new string 
    newstring += stringInput[0]
    # 3. go through each character in the string, and when i find a space character-> then put the character that comes after the space into the new string- > do this till we get to the end of the original string
    for i in range(0, len(stringInput), 1):
        if stringInput[i] == " " and stringInput[i+1] != " ":
            newstring += stringInput[i+1]
    # 4. return this new string
    return newstring.upper()


print(acronymGenerator("national   basketball  association"))
print(acronymGenerator("national football league"))


#“ Parens Valid
#Create a function that, given an input string str, returns a boolean whether parentheses in str are valid. Valid sets of parentheses always open before they close, for example. For "Y(3(p)p(3)r)s", return true. Given "N(0(p)3", return false: not every parenthesis is closed. Given "N(0)t )0(k", return false, because the underlined ")" is premature: there is nothing open for it to close.”

#Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.

def Valid(str):
    parens=[]
    for i in range(0,len(str)):
        if str[i] =='(':
            parens.append('(')
        elif str[i] ==')' :
            if not parens:
                return False
            else:
                parens.pop()
    if not parens:
        return True
    else:
        return False
print(Valid("Y(3(p)p(3)r)s"))
print(Valid("N(0(p)3"))
print(Valid("N(0)t )0(k"))

def parCheck(some_string):
    openCounter = 0
    closeCounter = 0
    for i in range(0, len(some_string), 1):
        if some_string[i] == "(":
            openCounter += 1
        if some_string[i] == ")":
            closeCounter += 1
        if closeCounter > openCounter:
            return "False"

    if openCounter == closeCounter:
        return "True"
    else:
        return "False"

print(parCheck("Y(3(p)p(3)r)s"))
print(parCheck("N(0(p)3"))
print(parCheck("N(0)t )0(k"))

# "h()(())" -> True 
# "(()))" -> False - unequal num of open vs closed
# "())(" -> False - invalid order

# 1. have some variables to represnt the open vs close count
# 2. look at EACH (hint: for loop) character in the string
    # a. IF i see a open p -> then increase the num of open by 1, same with close
    # if at any point the number of open parenthesis is less than closed parens- return false b/c premature closing symbol
# 3. by the time we get to end of the string, we have total for open vs close-> if open != closed - return false b/c uneven amount


def parensValid(stringInput):
    # 1. have some variables to represnt the open vs close count
    openP = 0
    closeP = 0
    # 2. look at EACH (hint: for loop) character in the string
    for i in range(0, len(stringInput), 1):
        # a. IF i see a open p -> then increase the num of open by 1, same with close
        if stringInput[i] == "(":
            openP += 1
        elif stringInput[i] == ")":
            closeP += 1
        # if at any point the number of open parenthesis is less than closed parens- return false b/c premature closing symbol
        if openP < closeP:
            return False
    # 3. by the time we get to end of the string, we have total for open vs close-> if open != closed - return false b/c uneven amount
    if openP != closeP:
        return False
    else:
        return True


print(parensValid("h()(())"))
print(parensValid("h()(())("))
print(parensValid("h())((())"))


#“ Coin Change with Object
#Given a number of U.S. cents, return the optimal configuration of coins, in an object.”

#Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks. 

def generateChange(num): 
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while num > 0:
        if num >= 25:
            quarters += 1
            num -= 25

        elif num >= 10:
            dimes += 1
            num -= 10

        elif num >= 5:
            nickels += 1
            num -=5

        elif num >= 1: 
            pennies += 1
            num -= 1

    print(f"Quarters: " + str(quarters))
    print(f"Dimes: " + str(dimes))
    print(f"Nickels: " + str(nickels))
    print(f"Pennies: " + str(pennies))


generateChange(26)

def genCoinChange(numCents):
    # change = {}
    numQuarters = numCents//25
    # change['q'] = numQuarters
    remaining = numCents - (numQuarters*25)
    numDimes = remaining//10
    # change['d'] = numDimes
    remaining = remaining - (numDimes*10)
    numNickles = remaining//5
    remaining = remaining - (numNickles*5)

    change = {"q": numQuarters, "d":numDimes, "n":numNickles, "p":remaining}
    return change


print(genCoinChange(64))


#Morning Algos:
Balance Point
Given an array, return true or false whether or not there is a balance point between indices where one side’s sum is equal to the other’s. (Example: [1,2,3,4,10] -> True (between indicies 3 and 4), but [1,2,3,4,5] -> false)

Balance Index
Given an array, return an index point in which the sums on either side of this index are equal to each other. Do NOT include the balance index in either sum. If none exists, return -1. (Example: [-2,5,7,0,3] -> 2 but [9,9] should return -1)


function balanceIndex(arr) {
    if (arr.length < 3) {
        return console.log("-1");
    }

    var indexVal = 0;

    for (var i = 1; i < arr.length; i++) {
        var sumLeft = 0;
        var sumRight = 0;
        // check left
        for (var j = 0; j < i; j++) {
            sumLeft += arr[j];
        }
        // console.log(sumLeft);
        // console.log("End of sumLeft");

        // check right
        for (var k = i + 1; k < arr.length; k++) {
            sumRight += arr[k];
        }
        // console.log(sumRight);
        // console.log("End of sumRight");
        if (sumLeft == sumRight) {
            indexVal = i;
            return console.log(
                `At index ${indexVal}, the array is balanced. Both sides equal ${sumLeft}!`
            );
        }
        // console.log("");
    }
    return console.log("-1");
}

balanceIndex([2]);
balanceIndex([2, 2]);
balanceIndex([1, 2, 3, 0, 3, 2, 1]);
balanceIndex([1, 2, 3, 0, 3, 2, 17]);