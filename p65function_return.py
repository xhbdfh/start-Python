def maximum(x,y):
    if x>y:
        return x
    elif x==y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2,3))

# 它是如何工作的
# maximum函数将会返回参数中的最大值，在本例中是提供给函数的数值。它使用一套简单的if...else语句来找到较大的那个值并将其返回。
# 要注意到如果return语句没有搭配任何一个值则代表着 返回None。None在Python中一个特殊的类型，代表着虚无。举个例子，它用于指示一个变量没有值，如果有值，则它的值是None(虚无)。
# 每一个函数都在其末尾隐含了一句return None，除非你写了你自己的return语句。你可以运行print(some_function()),其中some_function函数不使用return语句，就像这样：
# def some_function():
#     pass
# Python中的pass语句用于指示一个没有内容的语句块。
# 提示：有一个名为max的内置函数已经实现了"找到最大数"这一功能，所以尽可能地使用这一内置函数。