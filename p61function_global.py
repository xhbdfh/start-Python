x = 50

def func():
    global x
    print('x is',x)
    x = 2
    print('Changed global x to',x)

func()
print('Value of x is',x)

#  它是如何工作的
#  global语句用心声明 x 是一个全局变量——因此，当我们在函数中为x进行赋值时，这一改动将影响到我们在主代码块中使用的x的值。
#  你可以在同一句global语句中指定不止一个的全局变量，例如global x,y,z。