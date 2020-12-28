n = int(input("n: "))

# TODO. n의 소인수를 구해 출력하기

prime_list =[]
for i in range(2, n+1):
    
    # divisor
    if n%i == 0:
        
        # Prime number
        count = 1
        for j in range(2,i+1):
            if i%j ==0 :
                count += 1
        
        if count == 2:
            prime_list.append(i)
        
        
for prime_divisor in prime_list:
    print (prime_divisor)