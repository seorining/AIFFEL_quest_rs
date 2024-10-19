import random

# 5자리 이외의 숫자가 들어왔을 때 예외처리하기


class InputError(Exception):
    pass


def find_err(num_list):
    if len(num_list) != 5:
        raise InputError()


# 정답 5자리 숫자 중복없이 랜덤 생성
answer_list = []
for _ in range(5):
    num = random.randint(0, 9)
    while num in answer_list:
        num = random.randint(0, 9)
    answer_list.append(num)

# 사용자가 정답을 맞출 때까지 loop
# ctrl+c(keyboardinterrupt) -> break
while True:
    strike = 0
    ball = 0
    # print('정답: ', *answer_list)
    try:
        print('입력: ', end='')
        input_num_list = list(map(int, input()))
        find_err(input_num_list)
    except KeyboardInterrupt:
        print('프로그램을 종료합니다')
        break
    except:
        print('숫자 5자리를 입력해주세요')
        continue

    for i_idx, i_value in enumerate(input_num_list):
        for a_idx, a_value in enumerate(answer_list):
            if i_value == a_value:
                if i_idx == a_idx:
                    strike += 1
                else:
                    ball += 1

    print(f'{strike} strike, {ball} ball')
    print('--------------------')

    if strike == 5:
        print('정답!')
        break
