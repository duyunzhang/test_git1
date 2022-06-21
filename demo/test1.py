'''
@file :  test1.py
@author : 张福卫
@date : 2022/6/21 10:51
'''

book_list=['红楼梦','水浒传','西游记','三国演义']
def show_book():
    print('-'*10+'列表如下'+'-'*10)
    for x,i in enumerate(book_list):
        print('{}:《{}》'.format(x+1,i))

def add_books(book_name):
    if book_name!='':
        book_list.append(book_name)
        show_book()
        print('添加成功')
    else:
        print('请输入您要添加的书名！')

add_books('从你的全世界看路过')