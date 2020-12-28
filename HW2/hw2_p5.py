sentence = input("input sentence: ")

# TODO 1. split 함수를 이용해 sentence를 word에 list로 저장하기
wordlist = sentence.split()

# TODO 2. a/A 다음에 모음으로 시작하는 단어가 나올 때 an/An으로 바꾸기
word_count = dict()
vowels = ['a','e', 'i','o','u', 'A', 'E', 'I', 'O', 'U']
for i, word in enumerate(wordlist):
    
    if word == 'a':
        if wordlist[i+1][0] in vowels:
            wordlist[i] = 'an'
        
    elif word == 'A':
        if wordlist[i+1][0] in vowels:
            wordlist[i] = 'An'
            
    elif word == 'an':
        if wordlist[i+1][0] not in vowels:
            wordlist[i] = 'a'
    
    elif word == 'An':
        if wordlist[i+1][0] not in vowels:
            wordlist[i] = 'A'
            
        


# TODO 3. 관사 뒤에 오는 단어를 모두 명사라고 가정한 후 한 명사가 두 번째 사용될 때 부터 관사를 "The/the"으로 적용하기
            
following = []

for i, word in enumerate(wordlist):
    
    if word == 'a' or word == 'an':
        if wordlist[i+1] in following:
            wordlist[i] = 'the'
        else:
            following.append(wordlist[i+1])
        
    elif word == 'A' or word == 'An':
        if wordlist[i+1] in following:
            wordlist[i] = 'The'
        else:
            following.append(wordlist[i+1])
            



# TODO 4. 결과 출력하기
final_sentence =' '.join(wordlist)

print (final_sentence)