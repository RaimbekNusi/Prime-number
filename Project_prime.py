def is_prime(N):
    """
    Determines whether a given positive integer is prime or not
    input: N, any positive integer.
    returns: True if N is prime, False otherwise.
    """
    # special cases:
    if N == 1:
        return False

    # the biggest divisor we're going to try
    divisor = N // 2
    while divisor > 1:
        if N % divisor == 0:
            # we found a number that is a factor of N            
            return False
        divisor = divisor - 1
        
    return True

out = {}
def numbers(x):
    """
    Opens a numbers.txt file, reads all the numbers in the file,
    calls a is_prime function, caches the numbers (keys) and values True or False to dictionary "out"
    :param x: is a txt file, in this case numbers.txt
    returns: The dictionary "out" containing numbers from the file and values True or False,
    depending if the number is prime or non-prime respectively
    """
    f = open(x,"r")
    for line in f:
        out[int(line)] = is_prime(int(line))
    f.close()
    return out
x = input("Write the name of the .txt file")
print(numbers(x))


    
