# IMG = '../assert/captain/uat-switch.png'
#
# x, y, width, height = pyautogui.locateOnScreen(IMG, confidence=0.8)
# x, y = pyautogui.center((x, y, width, height))
# pyautogui.moveTo(x, y, duration=0.3)
# print(x, y)
#



class MyClass:
    # 这是一个静态变量
    static_var = "我是静态变量"

    def __init__(self):
        pass

    def print_static_var(self):
        # 在类的方法中访问静态变量
        print(MyClass.static_var)


# 创建 MyClass 的两个实例
instance1 = MyClass()
instance2 = MyClass()


# 访问静态变量
print(instance1.static_var)  # 输出: 我是静态变量
instance1.print_static_var()  # 输出: 我是静态变量

# 更改静态变量
MyClass.static_var = "我被修改了"
print(instance1.static_var)  # 输出: 我被修改了
instance1.print_static_var()  # 输出: 我被修改了


# 通过实例也可以修改静态变量，但这通常不是推荐的做法
instance1.static_var = "我不推荐这样做"
print(MyClass.static_var)  # 输出: 我被修改了 (注意这里没有变)
print(instance1.static_var)  # 输出: 我不推荐这样做 (instance1现在指向了一个实例属性)