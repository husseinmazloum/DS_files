## Version 1

n = 20
number_range = set(range(2, n+1))
primes_list = []


prime = min(sorted(number_range))
number_range.remove(prime)
primes_list.append(prime)
multiples = set(range(prime*2, n+1, prime))
number_range.difference_update(multiples)



## Version 2

## Upper Bound
n = 1000

## Number range to be checked
number_range = set(range(2, n+1))

## empty list to append discovered primes to 
primes_list = []

## While Loop

while len(number_range) >= 1:
    prime = min(sorted(number_range))
    number_range.remove(prime)
    primes_list.append(prime)
    multiples = set(range(prime*2, n+1, prime))
    number_range.difference_update(multiples)
    

## print our list of prime numbers

print("Primes List: ", primes_list)
    

## number of prime numbers that were found

primes_count = len(primes_list)


## largest prime number found

largest_prime = max(primes_list)

## Summary statement

print(f"There are {primes_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")


## Version 3a - slow when finding primes at 1 Million due to sorting in the while loop


def primes_finder(n):
    ## Number range to be checked
    number_range = set(range(2, n+1))

    ## empty list to append discovered primes to 
    primes_list = []

    ## While Loop
    while len(number_range) >= 1:
        prime = min(sorted(number_range))
        number_range.remove(prime)
        primes_list.append(prime)
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples)
        

    ## print our list of prime numbers
    #print("Primes List: ", primes_list)
        

    ## number of prime numbers that were found
    primes_count = len(primes_list)


    ## largest prime number found
    largest_prime = max(primes_list)

    ## Summary statement
    print(f"There are {primes_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")
    
    ## return the list of prime numbers as output when calling the function
    return primes_list

primes_finder(100)
primes_list = primes_finder(100)
print(primes_list)



primes_list = primes_finder(100000)



## Version 3b - faster than 3A due to using .pop() in the while loop. This is less accurate due to the 
## nature of sets being unordered. We cannot guarantee that the lowest value in the list will be selected 
## for .pop()


def primes_finder(n):
    ## Number range to be checked
    number_range = set(range(2, n+1))

    ## empty list to append discovered primes to 
    primes_list = []

    ## While Loop
    while len(number_range) >= 1:
        prime = number_range.pop()
        primes_list.append(prime)
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples)
        

    ## print our list of prime numbers
    #print("Primes List: ", primes_list)
        

    ## number of prime numbers that were found
    primes_count = len(primes_list)


    ## largest prime number found
    largest_prime = max(primes_list)

    ## Summary statement
    print(f"There are {primes_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")
    
    ## return the list of prime numbers as output when calling the function
    return primes_list


primes_list = primes_finder(10000)































































