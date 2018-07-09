from django.db import models
from article.models import Article
from user.models import User
# Create your models here.
class Comment(models.Model):
    text = models.TextField(verbose_name='评论内容')
    created_time = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey(Article,verbose_name='文章标题')
    user = models.ForeignKey(User,verbose_name='用户名')

    def __str__(self):
        return self.text[:20]


    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
