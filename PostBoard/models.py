from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import reverse
from django.utils import timezone

class Author(models.Model):
    user = models.OneToOneField(to = User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

class Category(models.Model):
    name = models.CharField(max_length = 64,unique = True,null = False,help_text= ('name_of_category_post'))

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    author_post = models.ForeignKey(to = Author,on_delete = models.CASCADE)
    time_in = models.DateTimeField(default= timezone.now())
    heading = models.CharField(max_length = 256 , null = False)
    text = models.TextField()
    category_post = models.ManyToManyField(Category, through='PostCategory')
    cover = models.ImageField(null = True , blank = True,upload_to = 'images/')

    def __str__(self):
        return f'{self.text}'

    def get_absolute_url(self):
        return reverse('post_detail',args = [str(self.id)])



class PostCategory(models.Model):
    post = models.ForeignKey(to = Post,on_delete = models.CASCADE)
    category = models.ForeignKey(to = Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(to = Post,on_delete = models.CASCADE)
    user = models.ForeignKey(to = User,on_delete = models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(default = timezone.now())
    rating = models.IntegerField(default = 0)

    def get_absolute_url(self):
        return reverse('comment_detail',args = [str(self.id)])

    def __str__(self):
        return f'{self.text} - {self.user}'

class Like(models.Model):
    user = models.ForeignKey(to = User,on_delete = models.CASCADE)
    comment = models.ForeignKey(to = Comment,default = False,on_delete = models.CASCADE)

    #def get_absolute_url(self):
        #return reverse('comment_detail',args = [str(self.id)]) + '/like'

