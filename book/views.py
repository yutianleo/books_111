import math
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *


# Create your views here.
# 登录页面
def loginview(request):
    if request.method == 'GET':
        return render(request, 'login.html')


# 所有图书的页面
def allbookview(request, num=1):
    # allbookList = MainprojectBooks.objects.all()
    # return render(request, 'allbook.html', {'allbookList': allbookList})
    num = int(num)
    # 查询所有书籍信息按id来排序
    bookslist = MainprojectBooks.objects.all()
    # 页码展示信息数量
    page_obj = Paginator(bookslist, 10)
    # 获取当前页码
    page_books_list = page_obj.page(num)
    # 页面中的所有页码数（页码列表）
    start = num - int(math.ceil(10.0 / 2))
    if start < 1:
        start = 1
    end = start + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages
    if end < 10:
        start = 1
    else:
        start = end - 9

    page_list = range(start, end + 1)
    # 传入的数据：当前页码的书籍和页码表
    return render(request, 'allbook.html', {'bookslist': page_books_list, 'page_list': page_list, 'num': num})


def indexview(request):
    return render(request, 'index.html')


# 排行榜的页面
def borrowbooktopview(request):
    stuList = MainprojectBooks.objects.all()
    return render(request, 'info.html', {'stuList': stuList})


# 还书页面
def returnbookview(request):
    return render(request, 'returnbook.html')


# 个人信息页面
def myinfoview(request):
    return render(request, 'myinfo.html')


# 查找图书页面
def findbookview(request):
    return render(request, 'findbook.html')


# 借书页面
def borrowbookview(request):
    return render(request, 'borrowbook.html')


# 修改个人信息页面
def changemyinfoview(request):
    return render(request, 'message.html')


# 逾期惩罚页面
def punishview(request):
    return render(request, 'punish.html')


# 儿童专区页面
def kidsview(request, num=1):
    num = int(num)
    booktype = MainprojectBooktype.objects.get(bt_id=1)
    bookslist = MainprojectBooks.objects.filter(bt_type_id=booktype).all()
    # 页码展示信息数量
    page_obj = Paginator(bookslist, 10)
    # 获取当前页码
    page_books_list = page_obj.page(num)
    # 页面中的所有页码数（页码列表）
    start = num - int(math.ceil(10 / 2))
    if start < 1:
        start = 1
    end = start + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages
    if end < 10:
        start = 1
    else:
        start = end - 9

    page_list = range(start, end + 1)
    # 传入的数据：当前页码的书籍和页码表
    return render(request, 'kids.html', {'bookslist': page_books_list, 'page_list': page_list, 'num': num})


# 教育专区页面
def educationview(request, num=1):
    booktype = MainprojectBooktype.objects.get(bt_id=4)
    bookslist = MainprojectBooks.objects.filter(bt_type_id=booktype).all()
    num = int(num)
    # 页码展示信息数量
    page_obj = Paginator(bookslist, 10)
    # 获取当前页码
    page_books_list = page_obj.page(num)
    # 页面中的所有页码数（页码列表）
    start = num - int(math.ceil(10.0 / 2))
    if start < 1:
        start = 1
    end = start + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages
    if end < 10:
        start = 1
    else:
        start = end - 9

    page_list = range(start, end + 1)
    # 传入的数据：当前页码的书籍和页码表
    return render(request, 'education.html', {'bookslist': page_books_list, 'page_list': page_list, 'num': num})


# 生活专区页面
def lifeview(request, num=1):
    booktype = MainprojectBooktype.objects.get(bt_id=2)
    bookslist = MainprojectBooks.objects.filter(bt_type_id=booktype).all()
    num = int(num)
    # 页码展示信息数量
    page_obj = Paginator(bookslist, 10)
    # 获取当前页码
    page_books_list = page_obj.page(num)
    # 页面中的所有页码数（页码列表）
    start = num - int(math.ceil(10.0 / 2))
    if start < 1:
        start = 1
    end = start + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages
    if end < 10:
        start = 1
    else:
        start = end - 9

    page_list = range(start, end + 1)
    # 传入的数据：当前页码的书籍和页码表
    return render(request, 'education.html', {'bookslist': page_books_list, 'page_list': page_list, 'num': num})


# 科技专区页面
def scienceview(request, num=1):
    booktype = MainprojectBooktype.objects.get(bt_id=3)
    bookslist = MainprojectBooks.objects.filter(bt_type_id=booktype).all()
    num = int(num)
    # 页码展示信息数量
    page_obj = Paginator(bookslist, 10)
    # 获取当前页码
    page_books_list = page_obj.page(num)
    # 页面中的所有页码数（页码列表）
    start = num - int(math.ceil(10.0 / 2))
    if start < 1:
        start = 1
    end = start + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages
    if end < 10:
        start = 1
    else:
        start = end - 9

    page_list = range(start, end + 1)
    # 传入的数据：当前页码的书籍和页码表
    return render(request, 'science.html', {'bookslist': page_books_list, 'page_list': page_list, 'num': num})


# 心愿单页面
def wish_listview(request):
    return render(request, 'wish_list.html')


# 关于我们页面
def about_ourview(request):
    return render(request, 'about_our.html')


def Contain(request):
    uname = request.POST.get('regi_user', '')
    pwd = request.POST.get('regi_pwd', '')
    a = user.objects.filter(uname=uname)
    if a:
        return HttpResponse(u'该用户已经注册')
    else:
        user.objects.create(uname=uname, pwd=pwd)
        return HttpResponseRedirect('/login/')


def index(request):
    uname = request.POST.get('lo_user', '')
    pwd = request.POST.get('lo_pwd', '')
    a = user.objects.filter(uname=uname, pwd=pwd)
    if a:
        return render(request, 'index.html')


def BackView(request):
    uname = request.POST.get('for_name', '')
    pwd = request.POST.get('for_pwd', '')
    user.objects.filter(uname=uname).update(pwd=pwd)
    return HttpResponseRedirect('/login/')


def MessageView(request):
    users = user.objects.all()
    return render(request, 'message.html', {'users': users})

def search(request,num):
    num = int(num)
    book_list = MainprojectBooks.objects.filter(bk_id=num).all()
    return render(request,'findbook.html',{'book_list':book_list})