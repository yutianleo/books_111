from django.shortcuts import render
from .models import *


# Create your views here.
# 登录页面
def loginview(request):
    return render(request, 'login.html')


# 所有图书的页面
def allbookview(request):
    allbookList = MainprojectBooks.objects.all()
    return render(request, 'allbook.html', {'allbookList': allbookList})


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
    return render(request, 'changemyinfo.html')


# 逾期惩罚页面
def punishview(request):
    return render(request, 'punish.html')


# 儿童专区页面
def kidsview(request):
    return render(request, 'kids.html')


# 教育专区页面
def educationview(request):
    return render(request, 'education.html')


# 生活专区页面
def lifeview(request):
    return render(request, 'life.html')


# 科技专区页面
def scienceview(request):
    return render(request, 'science.html')


# 心愿单页面
def wish_listview(request):
    return render(request, 'wish_list.html')


# 关于我们页面
def about_ourview(request):
    return render(request, 'about_our.html')


def search(request,num):
    num = int(num)
    book_list = MainprojectBooks.objects.filter(bk_id=num).all()
    return render(request,'findbook.html',{'book_list':book_list})