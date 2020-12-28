from hw3_p3 import make_snail
from hw3_p4 import print_mat


# You may add your own function(including the new rotation function) or import function from hw_p4.py

# TODO: Write a rotation function that rotate snail 45 degree
#       e.g. def rotate45(snail, rot_dir): ...


########### CHECK SHAPE ###########
def is_rectangle(snail):
    n = len(snail)
    
    if n == 1:
        return True
    
    elif n > 1:
        if len(snail[0]) == len(snail[1]):
            return True
        else:
            return False

########### PRINT ARRAY ###########
def print_dia(snail):
    n = int((len(snail)+1)/2)
    n_dia = len(snail)
    for i in range(n_dia):
        if i <= n-1:
            half_blank = n - i - 1
            print ("   "*half_blank, end = '')
            print ("   ".join( [f"{num:0>3}" for num in snail[i]] ), end = '')
            print ("   "*half_blank)
        
        else:
            half_blank = i - n + 1
            print ("   "*half_blank, end = '')
            print ("   ".join( [f"{num:0>3}" for num in snail[i]] ), end = '')
            print ("   "*half_blank)
        
def print_2d(snail):
    if is_rectangle(snail):
        print_mat(snail)
    else:
        print_dia(snail)


######### SUBFUNCTION ######
def rec_to_dia_CW(snail):
    n = len(snail)
    
    result = []
    for sum in range(n):
        l = []
        for j in range(sum+1):
            i = sum - j
            l.append(snail[i][j])
        result.append(l)
        
    for i in range(n-1):
        l = []
        sum = n + i
        for j in range(i+1, n):
            l.append(snail[sum-j][j])
        result.append(l)
        
    return result

def rec_to_dia_CCW(snail):
    
    n = len(snail)
    result = []
    for i in range(n):
        l = []
        for j in range(i+1):
            l.append(snail[j][j+n-1-i])
        result.append(l)
        
    for i in range(n-1):
        l = []
        for j in range(n-1-i):
            l.append(snail[j+1+i][j])
        result.append(l)
        
    return result

def dia_to_rec_CW(snail):
    n_rec = int((len(snail)+1)/2)

    result = [[-1 for x in range(n_rec)] for x in range(n_rec)]
    for i in range(n_rec):
        for j in range(len(snail[i])):
            result[j][j+n-1-i] = snail[i][j]

    for i in range(n_rec-1):
        for j in range(n_rec-1-i):
            result[j+1+i][j] = snail[n_rec + i][j]
        
    return result

      
def dia_to_rec_CCW(snail):

    n_rec = int((len(snail)+1)/2)
    result = [[-1 for x in range(n_rec)] for x in range(n_rec)]
    for i in range(n_rec):
        for j in range(i+1):
            result[i-j][j] = snail[i][j]
    for i in range(n_rec-1):
        for j in range(n_rec-1-i):
            result[n_rec-1-j][i+1+j]= snail[n_rec+i][j]
    return result

########### MAIN FUNCTION ############
def rotate_45(snail, rot_dir):
    
    
    if is_rectangle(snail) == True:
        
        if rot_dir == 'CW': 
            res  = rec_to_dia_CW(snail)
            
        else:
            res = rec_to_dia_CCW(snail)
        

    else:
        if rot_dir == 'CW':
            res = dia_to_rec_CW(snail)
        else:
            res = dia_to_rec_CCW(snail)
            
    return res
            


if __name__ == "__main__":
    n = int(input('Snail Size : '))
    direction = input('Direction : ')

    # TODO : Write down your code
    
    snail = make_snail(n, direction)
    print_2d(snail)
    
    rot_dir = input('Rotate: ')
    while rot_dir != 'END':
        result = rotate_45(snail, rot_dir)
        print_2d(result)
        snail = result

        rot_dir = input('Rotate: ')