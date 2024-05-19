def generate_fibonacci(n):
    seq = [0, 1]  # initial array with 0 and 1
    while len(seq) < n:  # loop until the sequence has n elements
        seq.append(seq[-1] + seq[-2])  # add the next element in the sequence
    return seq[:n]  # return the first n elements of the sequence

# Take input from the user
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_number = generate_fibonacci(n)
print(fib_number)
