
def generate_fibonacci(n):
    
    seq = [0,1]        # initial array with 0 and 1 #
    
    while len(seq) < n:      #loop till       
        
     seq.append(seq[-1]+ seq[-2])    #add an element at the end of the array by adding the prev two elemnt
        
    return seq[:n]

n = 10
fib_number = generate_fibonacci(n)
print(fib_number)
    