from django.db import models
from user.models import User
# Create your models here.

class Tag(models.Model):

    name = models.CharField(max_length=50,verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=100,verbose_name='分类')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=100,verbose_name='标题')
    data = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    content = models.TextField(verbose_name='文章内容')

    user = models.ForeignKey(User,verbose_name='用户')
    tag = models.ManyToManyField(Tag,verbose_name='标签')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-data']
    def __str__(self):
        return self.title