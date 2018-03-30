def say(message,times=1):
    print(message * times)

say('Hello')
say('World',5)

# 它是如何工作的
# 名为say的函数用心按照给定的次数打印一串字符串。如果我们没有提供一个数值，则将按照默认设置，只打印一次字符串。我们通过为参数times指定默认参数值1来实现这一点。
# 在第一次使用say时，我们只提供字符串因而函数只会将这一字符串打印一次。在第二次使用say时，我们即提供了字符串，同时也提供了一个参数5，声明我们希望说（say）这个字符串5次。