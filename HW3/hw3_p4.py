from hw3_p3 import make_snail

# You may add your own function

def print_mat(list2d):
    for row in list2d:
        for element in row:
            print (f"{element:0>3}", end = ' ')
        print ('')

def rotate(snail, rot_dir):
    """ 
    Return the 90 degree rotated 2D list of 'snail'.
        snail: 2D list
        rot_dir: direction of rotation ('CW' or 'CCW')
    """
    n = len(snail)
    result = [[-1 for x in range(n)] for x in range(n)]

    # TODO : Write down your code here.
    if rot_dir == 'CW':
        for i in range(n):
            for j in range(n):
                result[j][n-1-i] = snail[i][j]
                
    elif rot_dir == 'CCW':
        for i in range(n):
            for j in range(n):
                result[n-1-j][i] = snail[i][j]

    return result


if __name__ == "__main__":
    n = int(input('Snail Size: '))
    snail_dir = input('Direction: ')

    # TODO : Write down your code here.
    
    snail = make_snail(n, snail_dir)
    print_mat(snail)
    
    rot_dir = input('Rotate: ')
    
    while rot_dir != 'END':
        
        snail = rotate(snail, rot_dir)
        print_mat(snail)
        
        rot_dir = input('Rotate: ')