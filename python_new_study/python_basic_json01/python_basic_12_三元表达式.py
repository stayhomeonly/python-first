"""
#@Time：2022/6/25-10:28
#@file：python_basic_12_三元表达式
#@Project:python_new_study
#@Content:

"""
# 写一个功能比较两个数的大小
def func(x,y):
    if x>y:
        return x
    else:
        return y
x=6
y=7
res=func(x,y)
print(res)
# 用三元表达式的写法:条件成立返回的值 if 加一个条件 else 条件不成立的值,左侧可以是函数，也可以是值，右侧也是
res1=x if x>y else y
print(res1)
