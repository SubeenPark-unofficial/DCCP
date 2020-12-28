import json


def input_json(*prompt):
    json_str = input(*prompt)

    return json.loads(json_str)

######################

# 프로그램 입력으로 쓸 리스트 준비
# 1. 사용자 입력 없이 코드에서 바로 정의
# -> 주석 기호를 지우고 원하는대로 수정하여 사용하세요
data = [3, 5, 6, 3, 2, 9, 2, 5, 3, 7, 8]
target = [3, 7, 2, 8]
# (04/20 추가) 대신 아래 2번을 사용하려면 아래와 같이 각 변수에 None을 대입해주세요
# data = None
# target = None

# 2. 사용자 입력 받기
# -> 위의 리스트 선언을 주석처리하고(#), 아래와 같이 input() 대신 input_json()(위에서 정의)을 사용하세요
# (04/20 추가) 위의 코드 중 "None"을 대입하는 코드만 주석 해제하면, 아래 코드가 동작합니다
if data is None:
    data = input_json("Data? ")
if target is None:
    target = input_json("Target? ")


# TODO 아래에 코드를 작성하세요

count = [0]*len(target)

for i, tg in enumerate(target):
    count_tg = 0
    # Count number
    for dt in data:
        if dt == tg:
            count_tg += 1
    
    count[i] = count_tg
    
result = data[:]
for j, ct in enumerate(count):
    if ct > 2:
        for del_num in range(ct -2):
            result.remove(target[j])
    elif ct < 2:
        for add_num in range(2-ct):
            result.append(target[j])

print (result)
    


   

    
            
            
    
