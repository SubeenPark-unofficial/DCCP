def make_snail(n, dir):
    """
    Return the nxn 2D integer list following the rule of snail.
        n: size of list (nxn)
        dir: direction of snail ('CW' or 'CCW')
    """
    result = [[-1 for x in range(n)] for x in range(n)]

    # TODO : Write down your code here.
    i = 0
    j = 0
    
    if dir == 'CW':
        circ = 'r'
        
        for idx in range(n*n):
            result[i][j] = idx+1
        
            if circ == 'r':
                j += 1
        
                if j >= n-1 or result[i][j+1] != -1:
                    circ = 'd'
                    
            elif circ == 'd':
                i += 1
        
                if i >= n-1 or result[i+1][j] != -1:
                    circ = 'l'
                    
            elif circ == 'l':
                j -= 1
        
                if j <= 0 or result[i][j-1] != -1:
                    circ = 'u'
                    
            elif circ == 'u':
                i -= 1
        
                if i <= 0 or result[i-1][j] != -1:
                    circ = 'r'
                    
            
    if dir == 'CCW':
        circ = 'd'
        
        for idx in range(n*n):
            result[i][j] = idx+1
        
            if circ == 'r':
                j += 1

                if j >= n-1 or result[i][j+1] != -1:
                    circ = 'u'
                    
            elif circ == 'd':
                i += 1

                if i >= n-1 or result[i+1][j] != -1:
                    circ = 'r'
                    
            elif circ == 'l':
                j -= 1
        
                if j <= 0 or result[i][j-1] != -1:
                    circ = 'd'
                    
            elif circ == 'u':
                i -= 1

                if i <= 0 or result[i-1][j] != -1:
                    circ = 'l'

    return result
