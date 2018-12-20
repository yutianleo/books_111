# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


# 管理员注册类
class MainprojectAdminregister(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_name = models.CharField(max_length=30)
    a_pwd = models.CharField(max_length=30)
    a_sex = models.CharField(max_length=5)
    a_number = models.CharField(max_length=20)
    a_phone = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'mainproject_adminregister'


# 作者类
class MainprojectAuthors(models.Model):
    au_id = models.AutoField(primary_key=True)
    au_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mainproject_authors'


# 书类
class MainprojectBooks(models.Model):
    bk_id = models.AutoField(primary_key=True)
    bk_name = models.CharField(max_length=30)
    price = models.FloatField()
    intro = models.CharField(max_length=300)
    img = models.CharField(max_length=100)
    # 和作者的关系
    authors = models.ForeignKey(MainprojectAuthors, models.DO_NOTHING)
    # 和类型的关系
    bt_type = models.ForeignKey('MainprojectBooktype', models.DO_NOTHING)
    # 和出版社的关系
    presses = models.ForeignKey('MainprojectPress', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mainproject_books'


# 书的类型类
class MainprojectBooktype(models.Model):
    bt_id = models.AutoField(primary_key=True)
    bt_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mainproject_booktype'


# 借书类
class MainprojectBorrowBooks(models.Model):
    bb_id = models.AutoField(primary_key=True)
    bb_bdate = models.DateField()
    bb_rdate = models.DateField()
    # 和书的信息的关系
    bk_name = models.ForeignKey(MainprojectBooks, models.DO_NOTHING)
    # 和借书人的关系
    bp_name = models.ForeignKey('MainprojectBorrowPersons', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mainproject_borrow_books'


# 借书人类
class MainprojectBorrowPersons(models.Model):
    bp_id = models.AutoField(primary_key=True)
    bp_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mainproject_borrow_persons'


# 借书人 和 书 的中间表
class MainprojectBorrowPersonsBpBooks(models.Model):
    borrow_persons = models.ForeignKey(MainprojectBorrowPersons, models.DO_NOTHING)
    books = models.ForeignKey(MainprojectBooks, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mainproject_borrow_persons_bp_books'
        unique_together = (('borrow_persons', 'books'),)


# 出版社类
class MainprojectPress(models.Model):
    pr_id = models.AutoField(primary_key=True)
    pr_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mainproject_press'


# 职业类（注册用）
class MainprojectProfessions(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mainproject_professions'


# 用户注册类
class MainprojectUserregister(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30)
    upwd = models.CharField(max_length=30)
    usex = models.CharField(max_length=5)
    unumber = models.CharField(max_length=20)
    uphone = models.CharField(max_length=15)
    # 和职业类的关系
    bp_professions = models.ForeignKey(MainprojectProfessions, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mainproject_userregister'


class user(models.Model):
    uname = models.CharField(max_length=30)
    pwd = models.PositiveIntegerField()
