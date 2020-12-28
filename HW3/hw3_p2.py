import random

rand_num =[]
while len(rand_num) < 3:
    num = random.randint(1,9)
    if num not in rand_num:
        rand_num.append(num)
        
count = 5

print (f'Answer : {rand_num[0]} {rand_num[1]} {rand_num[2]}')

while count > 0:
    # recieve input
    nums = input(f"Trial No. {5-count+1} : ")
    l = [int(nums[0]), int(nums[2]), int(nums[4])]
    
    # reset vars
    out = 0
    strike = 0
    ball = 0
    
    # check conditions
    for i in range(3):
        if l[i] in rand_num:
            if l[i] == rand_num[i]:
                strike += 1
            else:
                ball += 1
        else:
            out += 1
            
    print (f"{strike} Strike {ball} Ball {out} Out")
            
    if out == 3:
        print ('You lose!')
        break
    
    if strike == 3:
        print ('You win!')
        
    count -= 1
    
if count == 0:
    print ('You lose!')
    

