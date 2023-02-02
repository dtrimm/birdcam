#############################################################


def isprime(n):
    """
    Check to see if number n is prime - return True or False
    No error checking on the number to make sure it is numeric
    """

    if n <= 1:
        return False
    elif n <= 3 :
        return True
    elif n % 2 == 0 or n % 3 == 0 :
        return False

    i = 5
    
    while i * i <= n :
        if n % i == 0 or n % (i + 2) == 0 :
            return False
        i = i + 6
    return True


#############################################################

def testit():
    """
    Prompt for a number and then return True if it is a prime,
    return False otherwise.
    """ 

    print("Prime Test")
    ns = input('Enter Number ->')

    if ns.isnumeric():
        n1 = int(ns) # convert to integer
        if isprime(n1):
            print("Yes\n")
            return(True)
        
    print("No\n") #if we got to here, then either not a prime or not a number
    return(False)




##############################################################


def primesinrange(s=0, e=1000, cnt=True, verbose=False):
    """
    Return either a list of the primes between s and e (if cnt=True)
    or a count of the number of primes between s and e (if cnt=False)
    verbose flag will give trace info if set to True

    """
    c=0  #counter
    l=[]
    if verbose:    #trace text
        print("start=%d\n" % s)
        print("end=%d\n" % e)
        
    for i in range(s,e):
        if isprime(i):
            if verbose: print(i)
            c=c+1               #one more found
            l=l+ [i] #add to list

    if verbose :
        print("There are %d primes between %d and %d\n" % (c, s, e))

    if cnt :
        return(c)  # return the count of the primes
    else :
        return(l) # return the list of the primes found
    



#############################################################

def fib(s=1, e=1):
    """
Return the fibonacci numbers between s and e (i.e. the sth number thru the eth
No error checking on whether s or e are numbers
if Verbose is True then a trace is output
    """

    if e < s:
        e = s

    print("start=%d\n" % s)
    print("end=%d\n" % e)

    n1=1 
    n2=0
    c=0 # general purpose counter
    l=[] #start off with an empty list
    
    if s <= 0: #positive non-zero start number required
        return []        
    
    while c < e:
        f = n1 + n2 # generate the next number in the series
        print("c=%d f=%d n1=%d n2=%d\n" % (c,f,n1,n2))
        n1 = n2
        n2 = f
        c = c + 1 # increment count - we've seen one more number
        if c >= s: # if this number is within the range, then add to the list
            l = l + [f]

        
    c=0
    for i in l: c=c+1 # count items in list
    
    if c==1:
        return l[0] # just one item, return the item
    else:
        return l # more than one item, return the list
    
      
#########################################################
