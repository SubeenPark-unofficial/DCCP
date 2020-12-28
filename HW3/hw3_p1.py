# 함수명은 변경하지 말 것. 함수의 매개변수 data는 변경 가능.
def mean(data):
    #TODO : Write down your code here.
    res = f"{sum(data)/len(data):.1f}"
    return res

def median(data):
    #TODO : Write down your code here.
    if len(data)%2 == 0: #even
        data.sort()
        res = (data[int(len(data)/2)-1] + data[int(len(data)/2)])/2
    
    else: # odd
        data.sort()
        res = data[(len(data)-1)/2]
    return res

def mode(data):
    #TODO : Write down your code here.
    count = {k:0 for k in set(data)}
    
    for d in data:
        count[d] += 1
            
    i = 0
    go = True
    while go:
        if count[data[i]] == max(count.values()):
            go = False
            return data[i]
        i += 1

def stdev(data):
    #TODO : Write down your code here.
    avg = sum(data)/len(data)
    s = 0
    for d in data:
        s += (d-avg)**2
    res = (s/(len(data)-1))**0.5
    return f"{res:.3f}"

def variance(data):
    #TODO : Write down your code here.
    avg = sum(data)/len(data)
    s = 0
    for d in data:
        s += (d-avg)**2
    res = s/(len(data)-1)
    return f"{res:.3f}"
