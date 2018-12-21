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
    uname = request.POST.get('lo_user', '')
    pwd = request.POST.get('lo_pwd', '')
    a = user.objects.filter(uname=uname, pwd=pwd)
    if a:
        request.session['login_uname'] = uname
        return render(request, 'index.html')


# 排行榜的页面
def borrowbooktopview(request):
    stuList = MainprojectBooks.objects.all()
    return render(request, 'phb.html', {'stuList': stuList})


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
    return render(request, 'life.html', {'bookslist': page_books_list, 'page_list': page_list, 'num': num})


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
        return HttpResponseRedirect('/index/login/')

def BackView(request):
    uname = request.POST.get('for_name', '')
    pwd = request.POST.get('for_pwd', '')
    user.objects.filter(uname=uname).update(pwd=pwd)
    return HttpResponseRedirect('/index/login/')


def MessageView(request):
    users = user.objects.all()
    return render(request, 'message.html', {'users': users})


def search(request,num):
    num = int(num)
    book_list = MainprojectBooks.objects.filter(bk_id=num).all()
    return render(request,'findbook.html',{'book_list':book_list})


# 管理员登录页面
def Administratorview(request):
    return render(request, 'administrator_index.html')


# 管理员登陆后的增加图书页面
def add_booksview(request):
    return render(request, 'add_books.html')


# 管理员登陆后的修改个人信息的页面
def change_administrator_infoview(request):
    return render(request, 'change_administrator_info.html')


def book(request, num):
    num = int(num)
    book_list = MainprojectBooks.objects.filter(bk_id=num).all()
    return render(request, 'book.html', {'book_list': book_list})


def Borrow_BookView(request):
    allbookList = MainprojectBooks.objects.all()
    return render(request,'borrow_book.html',{'allbookList': allbookList})



def BorrowView(request):
    uname=request.POST.get('uname','')  #借书人名字
    bookname=request.POST.get('bookname','') #书名
    bknum=request.POST.get('bknum','') #书的编号
    bbnum=request.POST.get('bbnum','') # 书的数量
    bbdate=request.POST.get('bbdate','') #借书日期
    brdate=request.POST.get('brdate','') # 还书日期
    bkname=MainprojectBooks.objects.get(bk_name=bookname)
    person=MainprojectBorrowPersons.objects.create(bp_name=uname)
    MainprojectBorrowBooks.objects.create(bb_id=bknum,bb_bdate=bbdate,bb_rdate=brdate,bk_name=bkname,bp_name=person)
    return HttpResponse(u"借阅成功")

def PermesView(request):
    uname=request.POST.get('uname','')
    phone=request.POST.get('phone','')
    postbox=request.POST.get('postbox','')
    identify=request.POST.get('identify','')
    sex=request.POST.get('sex','')
    job=request.POST.get('job','')
    profession=MainprojectProfessions.objects.create(p_name=job)
    profession.save()
    MainprojectUserregister.objects.create(uname=uname,unumber=identify,uphone=phone,bp_professions=profession,postbox=postbox,sex=sex)
    return HttpResponse(u"完善信息成功")


def backbookView(request):
    uname=request.POST.get('uname','')
    if uname == '':
        return HttpResponse('你没有借任何书籍')
    person=MainprojectBorrowPersons.objects.get(bp_name=uname)
    books=MainprojectBorrowBooks.objects.get(bp_name=person)
    bookname=books.bk_name.bk_name

    RetBook=MainprojectBooks.objects.get(bk_name=bookname)
    return render(request,'back.html',{"books":books,"RetBook":RetBook})


def successView(request):
    return HttpResponse(u'归还成功')


def showinfoView(request):
    mes=MainprojectUserregister.objects.filter(uname='谷茂鑫')
    return render(request,'showinfo.html',{'meses':mes})

