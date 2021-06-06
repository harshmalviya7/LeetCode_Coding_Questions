

def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

if __name__=="__main__":

    number=25
    curr=2
    while(number):
        if isprime(curr):
            print(curr,end=" ")
            number-=1
        curr+=1