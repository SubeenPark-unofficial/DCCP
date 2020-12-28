# 좌표의 수 N의 값 입력 받기
N = int(input())

# TODO write yout code below
# TODO 아래에 코드를 작성하세요

coords = []

for i in range(N):
    info = dict()
    xy= [int(num) for num in input().split()]
    info['x'] = xy[0]
    x = xy[0]
    info['y'] = xy[1] 
    y = xy[1]
    info['r'] = xy[0]**2 + xy[1]**2
    
    
    # Quadrant 
    if x == 0 and y == 0:
        info['quad'] = 0 # origin
        
    if x > 0 and y == 0:
        info['quad'] = 1 # x-axis: plus
    
    if x>0 and y>0:
        info['quad'] = 2 # quad1
        
    if x==0 and y>0:
        info['quad'] = 3 # y-axis: plus
        
    if x<0 and y>0:
        info['quad'] = 4 # quad2
        
    if x<0 and y==0:
        info['quad'] = 5 # x-axis: minus
        
    if x<0 and y<0:
        info['quad'] = 6 # quad3
        
    if x==0 and y<0:
        info['quad'] = 7 # y-axis: minus
        
    if x>0 and y<0:
        info['quad'] = 8 # quad4
    
    # tangent 
    if info['quad'] in [0, 1, 3, 5, 7]:
        info['atan'] = 0
    elif info['quad'] in [2, 6]:
        info['atan'] = y/x
    elif info['quad'] in [4, 8]:
        info['atan']= -(x/y)
        
    coords.append(info)
    
#print ("coords", coords, end='\n\n') ######## del before submission

# Sort by r
radius = [info['r'] for info in coords]
radius = sorted(list(set(radius)))
#print ("radius", radius, end='\n\n') ########## del before submission 

coords_r = dict()
for r in radius:
    coords_r[r] = []

for info in coords:
    coords_r[info['r']].append(info)
    
coords = coords_r

#print("coords_r", coords , end='\n\n')  
    
# Sort by quad 
for r in radius:
    infos_r = coords[r]
    
    quads_r = [d['quad'] for d in infos_r]
    quads_r = sorted(list(set(quads_r)))
    
    info_q = dict()
    for q in quads_r:
        info_q[q] = []
        
    for info in infos_r:
        info_q[info['quad']].append(info)
        
    coords[r] = info_q
    
# print ("coords_r_q", coords, end='\n\n')

# Sort by atan

for r in radius:
    infos_r = coords[r] 
    quads_r = list(infos_r.keys())
    
    for q in quads_r:
        infos_rq = infos_r[q]
        atan_rq = [d['atan'] for d in infos_rq]
        atan_rq = sorted(list(set(atan_rq)))
        
        info_a = dict()
        for atan in atan_rq:
            info_a[atan] = []
            
        for info in infos_rq:
            info_a[info['atan']].append(info)
            
        coords[r][q] = info_a
        
# print ("coords_r_q_a", coords, end='\n\n')
            
        
for r in list(coords.keys()):
    for q in list(coords[r].keys()):
        for atan in list(coords[r][q].keys()):
            info = (coords[r][q][atan][0])
            print (info['x'], info['y'])
            
    
            

            
        
    
    
        

    
    
        
        
    

    
