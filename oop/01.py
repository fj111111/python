'''
创建一个学生类
'''


# 定义一个空类
class Student():
    # 一个空类必须有代码
    # 用pass站位
    pass


# 定义一个对象
mingyue = Student()


# 定义一个Python学生的类
class PythonStudent():
    name = None
    age = 10
    course = 'Python'

    def doHomework(self):
        self.name
        self.age
        self.course
        print('i 在做作业')
        # 函数末尾推荐使用reutrn
        return None


# 实例化类
lili = PythonStudent()
print(lili.name)
print(lili.age)
lili.doHomework()


print(PythonStudent.__dict__)
