"""
#@Time：2022/6/25-10:28
#@file：python_basic_12_三元表达式
#@Project:python_new_study
#@Content:

"""
# 列表生成式
list1 = ['康师傅_老坛酸菜', '统一_老坛酸菜', '大金野_老坛酸菜', '白象']
new_list = []
# 找出里面已老坛酸菜结尾的
for name in list1:
    if name.endswith('老坛酸菜'):  # engswith就是已XX结尾的，择添加进去
        new_list.append(name)
print(new_list)
# 列表生达式写法
new_l = [name for name in list1 if name.endswith('老坛酸菜')]
print(new_l)
