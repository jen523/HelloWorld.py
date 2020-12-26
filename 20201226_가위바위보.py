import random
int_list = [1,2,3]

while (True):
    print("가위=1. 바위=2, 보=3 중에서 입력하세요:", end=" ")
    user_input = int(input())
    comp_input = random.choice(int_list)

    #print(user_input, comp_input)
    print('user_input:{}, comp_input:{}'.format(user_input, comp_input))

    #user_input에 대한 조건문 처리
    winner = ''

    if user_input == 1: # 1= 가위
        if comp_input == 1:
            winner = 'same'
        elif comp_input == 2:
            winner = 'comp'
        else:
            winner = 'user'
    elif user_input == 2: # 2= 바위
        if comp_input == 1:
            winner = 'user'
        elif comp_input == 2:
            winner = 'same'
        else:
            winner = 'comp'
    else: # 3 = 보
        if comp_input == 1:
            winner = 'comp'
        elif comp_input == 2:
            winner = 'user'
        else:
            winner = 'same'
    # print game result
    if winner == 'same':
        print('무승부')
    else:
        print('The game result is : {} 승리!' .format(winner))
