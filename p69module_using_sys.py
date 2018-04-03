import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is',sys.path,'\n')

# 跟案例输出结果不太一样，是因为windows跟MacOS的区别吗？好尴尬。。。