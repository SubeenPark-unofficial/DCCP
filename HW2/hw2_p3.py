import json


def input_json(*prompt):
    json_str = input(*prompt)

    return json.loads(json_str)


######################

# 프로그램 입력으로 쓸 리스트 준비
# -> 문제 2와 같습니다. 문제 2의 설명을 참고하세요.
p = {1: 2, 3: 1, 5: 7, 8: 16}
q = {1: 2, 5: 14, 6: 12, 8: 24}
#p = None
#q = None

if p is None:
    p = input_json("First dict? ")
if q is None:
    q = input_json("Second dict? ")
    

# TODO write your code below
# TODO 아래에 코드를 작성하세요
    
p_keys = list(p.keys())
q_keys = list(q.keys())
new_dict = dict()

for key in p_keys:
    if key in q_keys:
        new_dict[key] = 0

new_keys = list(new_dict.keys())

for key in new_keys:
    num_p = p[key]
    num_q = q[key]
    gcd = 1
    
    for div in range(1, min(num_p, num_q)+1):
        if num_p%div == 0 and num_q%div == 0:
            gcd = div
            
    new_dict[key] = gcd
    
print (new_dict)
    
    

