def numberOfBits(n):
    count = 0
    
    # right shift the number until it becomes a 0
    while (n):
        count+=1
        n >>= 1
        
    return count

number = int(input("Enter your number: "))
print("Total Bits: ", numberOfBits(number))