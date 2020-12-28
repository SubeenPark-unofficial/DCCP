##### 2020-1 DCCP Assignment 4
# OMOK.py skeleton code
# - 아래 skeleton code를 기반으로 문제 조건을 만족할 수 있도록 코드를 작성하세요.
# - 필요에 따라 member function을 추가하거나, 주어진 member function의 인자 및 return 값을 변경할 수 있습니다.
#   또는 필요하지 않다면 주어진 skeleton code의 member function을 사용하지 않을 수 있습니다.
# - 본인이 작성한 code의 동작을 설명하는 comment를 자세히 작성하세요.

import random


class OMOK():
    def __init__(self):
        self.width = 10
        self.height = 10
        self.grid = []
        self.record = []       
                                
                            

    def init_grid(self): 
        """ 바둑판 초기화

        self.width * self.height 크기의 바둑판을 생성하고 모든 칸을 '+'로 초기화한다.
        """
        self.grid = [
            ['+' for x in range(0, self.width)]
            for y in range(0, self.height)]

    # TODO: print_grind
    def print_grid(self):
        """ 현재 게임 상황(바둑판)을 출력

        '+': 돌이 놓여지지 않은 빈 칸
        'O': 사용자
        'X': 컴퓨터
        각 칸 사이에 공백 1개씩 출력해주세요.
          e.g.) + + + O + + X + ...
        """
        for row in self.grid:
            for entry in row:
                print (entry, end =' ')
            print ()
                
                
    # TODO: save
    def save(self):
        """ 현재까지 게임 진행 상황을 저장

        """
        # 입력 받은 파일명을 제목으로 가지는 파일을 작성
        # 플레이 기록은 (x_player, y_player);(x_computer, y_computer) \n 와 같이 한 줄에 한 번의 플레이 기록이 저장된다
        save_filename = input('[Type the name of replay file] : ')
        with open(save_filename, 'w') as record:
            for trial in range(0, len(self.record), 2):
                record.write(f"{self.record[trial]};{self.record[trial+1]}\n")
                

    # TODO: replay
    def replay(self):
        """ 오목 게임 replay

        이전에 (save 함수를 통해) 저장했던 게임을 읽어와 게일 기록을 출력한다.
        """
        while True:
            replay_filename = input('[Type the name of replay file or EXIT] : ')
            replay_file_opened = False
            
            # EXIT을 선택할 경우 메인 메뉴로 돌아가기 
            if replay_filename == 'EXIT': 
                self.menu()
                break
                
            # 파일 읽기
            else: 
                while not replay_file_opened:
                    try:
                        with open(replay_filename, 'r') as replay_file:
                            replay_file_opened = True 
                            trials = [line.rstrip().split(';') for line in replay_file.readlines()] # 불러온 파일에 기록된 모든 플레이 기록
                            self.init_grid()
                            
                            for trial in trials: 
                                # 특정 플레이의 player의 수 출력, grid에 업데이트
                                x, y = int(trial[0][1]), int(trial[0][4])
                                print (f"You add a stone at ({x}, {y})")
                                self.grid[y][x] = 'O'
                                self.print_grid()
                                # 특정 플레이의 computer의 수 출력, grid에 업데이트
                                x, y = int(trial[1][1]), int(trial[1][4])
                                print (f"Computer add a stone at ({x}, {y})")
                                self.grid[y][x] = 'X'
                                self.print_grid()
                    
                    # 파일이 존재하지 않을 경우 입력을 다시 받기
                    except IOError:
                        print (f"[Error: Can't find such file] - {replay_filename}")
                        replay_filename = input('[Type the name of replay file or EXIT] : ')
                
                    


    # TODO: menu
    def menu(self):
        """ 메뉴 화면 출력

        메뉴 화면을 출력하고 [사용자 입력]에 따라 다음 동작을 결정한다.
            1:          오목 게임 실행 (self.play())
            2:          replay 실행 (self.replay())
            3:          프로그램 종료
            otherwise:  에러 메시지 출력 후 메뉴 화면 출력
        """
        # 사용자 입력 받기
        right_input = False
        while not right_input:
            action = input('[Menu] (1) Start (2) Replay (3) End')
            if action in ['1', '2', '3'] and action.isdigit(): #숫자로 이루어진 경우인지 먼저 확인 후 형변환
                action = int(action)
                break
            else:
                print ('[Error - Please Type 1~3')
            
        # 사용자가 선택한 다음 단계로 진행
        if action == 1:
            self.play()
        elif action == 2:
            self.replay()
        elif action == 3:
            print ("Bye Bye '_' ")
            return 
            
        

    # TODO: play
    def play(self):
        
        """ 오목 게임 실행 (OMOK.py와 동일)

        오목 게임을 실행한다. 아래 동작들이 포함되어야 한다.
            - 사용자 입력을 받아 바둑판에 돌을 위치 (EXIT 처리 포함)
            - 사용자 돌을 놓은 후 바둑판 출력
            - 사용자 승리 조건 확인
            - 컴퓨터 돌을 놓은 후 바둑판 출력
            - 컴퓨터 승리 조건 확인

        프로그램 구현에 따라 위의 각 사항들은 user_turn, ai_turn 등의 다른 함수 내에서 처리할 수 있다.
        """
        print ("['START GAME']")
        self.init_grid() # 그리드 초기화
        turn = 0 # turn이 0일 경우 플레이어가, 1일 경우 컴퓨터가 플레이
        game_over = False
        
        while not game_over:
            
            # 플레이어 차례
            if turn == 0:
                loc = self.user_turn() #SAVE, EXIT 또는 x, y 좌표를 받음
                if loc == 'SAVE' or loc == 'EXIT': 
                    break # 메인 메뉴로의 복귀는 user_turn에 포함
                else:
                    x, y = loc
                
                # 게임 계속 실행
                if not self.is_over(x, y):
                    turn += 1 # 컴퓨터에게 턴을 넘긴다
                    
                # 게임 종료
                else:
                    game_over = True
                    self.game_over('player') # 승부가 날 시 결과를 나타내고 메뉴로 돌아감
                    self.menu()
                    
            
            # 컴퓨터 차례
            if turn == 1:
                
                # 게임 계속 실행
                x, y = self.ai_turn() #SAVE, EXIT 또는 x, y 좌표를 받음
                if not self.is_over(x, y):
                    turn -= 1 # 플레이어에게 턴을 넘긴다
                else:
                    game_over = True
                    self.game_over('computer') # 승부가 날 시 결과를 나타내고 메뉴로 돌아감
                    self.menu()
                    
        
    # 게임 진행 중 사용자 입력        
    def get_user_input(self):
        
        right_input = False

        while not right_input:
            loc = input('[Type the location(x, y) of your EXIT of SAVE]')

            # 메인메뉴로의 복귀는 User_turn에 포함
            if loc == 'SAVE' or loc == 'EXIT':
                right_input = True
                return loc # Return next action

            # 좌표 형태 확인
            # 공백 포함 3자 + 개행문자로 이루어져 있을 것 & 공백 좌우의 문자가 숫자일 것
            elif len(loc) == 4 and loc[1:3] == ', ' and loc[0].isdigit() and loc[-1].isdigit():  
                    if self.grid[int(loc[-1])][int(loc[0])] == '+': # 형식은 맞으나 중복일 경우
                        right_input = True
                        return int(loc[0]), int(loc[-1]) #x, y 좌표 반환
                    else:
                        print('[That location is already occupied]')
            else: 
                print ('[There are errors in your input]')

    # TODO: user_turn
    def user_turn(self):
        user_input = self.get_user_input()
        
        # 진행 상태 저장
        if user_input == 'SAVE':
            self.save()
            return 'SAVE'
        
        # 메인 메뉴로 복귀
        elif user_input == 'EXIT':
            self.menu()
            return 'EXIT'
        
        # 수 두기
        else:
            x, y = user_input
            print (f"You add a stone at ({x}, {y})")
            self.grid[y][x] = 'O' # x, y 좌표는 nested list indexing에서는 순서가 반대가 되니 조심할 것!
            self.print_grid()
            self.record.append(user_input) #게임 과정 기록
            return x, y
            

    # TODO: ai_turn
    def ai_turn(self):
        right_input = False
        
        while not right_input:
            loc = [random.randint(0, 9) for i in range(2)] #랜덤한 입력 받기
            if self.grid[int(loc[0])][int(loc[-1])] == '+': #중복일 경우 아닐 때까지 입력을 받음
                right_input = True 
                
        print (f"Computer add a stone at ({loc[1]}, {loc[0]})")
        self.grid[loc[0]][loc[1]] = 'X'
        self.print_grid()
        self.record.append((loc[0], loc[1])) #게임 과정 기록
        return loc[0], loc[1]

    def check_diagonal(self, x, y): # 좌측 상단에서 우측 하단 방향을 잇는 대각선/우측 상단에서 좌측 하단을 연결하는 대각선
        marker = self.grid[x][y]
        
        # to upper left from now
        ul = 1 
        ul_count = 0 # 
        while not (x-ul<0 or y-ul<0):
            if self.grid[x-ul][y-ul] == marker:
                ul_count += 1
                ul += 1
            else:
                break
                
        # to lower right from now
        lr = 1 
        lr_count = 0 # 
        while not (x+lr > 9 or y+lr >9):
            if self.grid[x+lr][y+lr] == marker:
                lr_count += 1
                lr += 1
            else:
                break
                
        # to lower left from now
        ll = 1
        ll_count = 0
        while not (x + ll > 9 or y -ll <0):
            if self.grid[x+ll][y-ll] == marker:
                ll_count += 1
                ll += 1
            else:
                break
                
        # to upper right from now
        ur = 1
        ur_count = 0
        while not (x - ur < 0 or y + ur >9):
            if self.grid[x-ur][y+ur] == marker:
                ur_count += 1
                ur += 1
            else:
                break
                
        return (ul_count + lr_count == 4) or (ll_count + ur_count == 4) #이번 턴에 둔 수를 포함해서 정확히 다섯개가 나열되도록 제약조건
    
    def check_vertical(self, x, y):
        marker = self.grid[y][x]
        
        # upper side
        u = 1
        u_count = 0
        while not (y-u < 0):
            if self.grid[y-u][x] == marker:
                u_count += 1
                u += 1
            else:
                break
        
        #down side
        d = 1
        d_count = 0
        while not (y+d > 9):
            if self.grid[y+d][x] == marker:
                d_count += 1
                d += 1
            else:
                break
                
        return (u_count + d_count == 4)
    
    def check_horizontal(self, x, y):
        marker = self.grid[y][x]
        
        # left side
        l = 1
        l_count = 0
        while not (x-l < 0):
            if self.grid[y][x-l] == marker:
                l_count += 1
                l += 1
            else:
                break
        
        # right side
        r = 1
        r_count = 0
        while not (x+r > 9):
            if self.grid[y][x+r] == marker:
                r_count += 1
                r += 1
            else:
                break
                
        return (l_count + r_count == 4)
            
        

    # TODO: is_over
    def is_over(self, x, y):
        """ 승리 조건 확인

        가장 최근에 놓은 돌의 x, y 좌표를 인자로 받아 승리 조건이 만족 되었는지를 확인 후 그 결과를 반환한다.
        :param
            x: 가장 최근에 놓은 돌의 x 좌표
            y: 가장 최근에 놓은 돌의 y 좌표
        :return
            승리 조건이 만족 되었다면 True, 그렇지 않다면 False
        """
        # 대각선, 가로, 세로 중 하나라도 참이 될 시 True(게임 종료)
        return self.check_diagonal(x, y) or self.check_horizontal(x, y) or self.check_vertical(x, y)


        

    # TODO: game_over
    def game_over(self, user_win):
        """ 게임 종료 메시지 출력

        user_win에 따라 알맞은 게임 종료 메시지를 출력한다.
        :param
            user_win: 사용자가 승리했을 경우 True, 컴퓨터가 승리했을 경우 False
        """
        # 당시 수를 둔 플레이어의 우승을 알리는 메시지 출력
        if user_win == 'computer':
            print ("[DEFEAT : You lose the game]")
        
        else:
            print ("[VICTORY : You win the game]")
        



# 아래에 main 함수 작성 (main 함수 외부에 코드 작성 금지)
# hint: 과제 기술 및 skeleton code 양식을 따를 경우, OMOK instance의 menu() 함수를 호출해 게임을 시작.
if __name__ == '__main__':
    game = OMOK()
    game.menu()
    



