# 包含一个学生类，一个sayhello函数，一个打印语句
class Student():
    def __init__(self, name='no', age=18):
        self.name = name
        self.age = age
    def say(self):
        print('My name is {0}'.format(self.name))
def sayHello():
    print('hi 欢迎来到')

# 此判断语句建议作为程序的入口
if __name__ == '__main__':
    print('我是p01')