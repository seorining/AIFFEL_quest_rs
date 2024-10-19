import random
import names


class Dormitory:
    point = 0
    name = ''

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_point(self):
        self.point += 1

    def lose_point(self):
        self.point -= 1

    def print_point(self):
        print(f'{self.name}의 점수는 {self.point}점!')


class person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def introduce(self):
        print(f'{self.name}는 {self.age}세 {self.sex}!')


class wizard(person):
    def __init__(self, name, age, sex, dormitory):
        super().__init__(name, age, sex)
        self.dormitory = dormitory

    def introduce(self):
        print(f'{self.name}는 {self.age}세 {self.sex} {self.dormitory.get_name()}!')

    def action(self, action):
        if action == 0:
            self.dormitory.get_point()
        elif action == 1:
            self.dormitory.lose_point()
        else:
            pass


dormitorys = [Dormitory('그리핀도르'), Dormitory(
    '슬리데린'), Dormitory('래번클로'), Dormitory('후플푸프')]
wizards = []

# 20명 랜덤 생성
for _ in range(20):
    name = names.get_full_name()
    age = random.randint(10, 30)
    sex = random.randint(0, 1)
    if sex == 0:
        sex = '남자'
    else:
        sex = '여자'
    dormitory = random.randint(0, 3)

    wizards.append(wizard(name, age, sex, dormitorys[dormitory]))

# 20명 소개
for magicion in wizards:
    magicion.introduce()

# 20명이 각자 랜덤한 행동 10번을 취함
for magicion in wizards:
    for i in range(10):
        action = random.randint(0, 2)
        magicion.action(action)

# 기숙사의 최종 점수 출력
for dormitory in dormitorys:
    dormitory.print_point()
    print(f'{dormitory.get_name()} 기숙사에 소속된 사람은 : ', end='')
    for magicion in wizards:
        if magicion.dormitory.get_name() == dormitory.get_name():
            print(f'[{magicion.name} {magicion.age}세{magicion.sex}] ', end='')
    print()
