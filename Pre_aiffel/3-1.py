import random


class person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def introduce(self):
        print(f'{self.name}는 {self.age} {self.sex}!')


class wizard(person):
    def __init__(self, name, age, sex, dormitory):
        super().__init__(name, age, sex)
        if dormitory == 0:
            self.dormitory = '그리핀도르'
        elif dormitory == 1:
            self.dormitory = '슬리데린'
        elif dormitory == 2:
            self.dormitory = '래번클로'
        else:
            self.dormitory = '후플푸프'

    def introduce(self):
        print(f'{self.name}는 {self.age} {self.sex} {self.dormitory}!')


dormitory = random.randint(0, 3)
name, age, sex = input('입력: ').split(', ')

randman = wizard(name, age, sex, dormitory)
randman.introduce()
