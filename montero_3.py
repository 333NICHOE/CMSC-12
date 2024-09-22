def fictitiousRoot(n):

    if n < 10:
        product = n
    
    else:

        while n > 10:
            product = 1

            while n > 0:
                last = n % 10
                product  = product * last
                n = n // 10
            n = product

    return product

n = int(input("Enter a number: "))

print(fictitiousRoot(n))