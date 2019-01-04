# coding=utf-8
# option+command+l 自动对其
class People:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def test(self):
        print self.name, self.age, self.sex


pop = People('小明', '男', 12)
pop.test()
