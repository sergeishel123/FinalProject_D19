from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail,mail_managers
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from .models import Comment,Post,Like

@receiver(post_save,sender = Comment)
def created_comment(sender,instance,created,**kwargs):
    post = Post.objects.get(id=instance.post_id)
    email = post.author_post.user.email
    if created:
        message = f'New Comment: {instance.text},{instance.user.username}'
        send_mail(
            subject='New Comment on your post!',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email]
        )
    else:
        subject = f'Comment changed for {instance.text},{instance.user.username}'


@receiver(post_delete,sender = Comment)
def deleted_comment(sender,instance,**kwargs):
    email = instance.user.email
    post = Post.objects.get(id = instance.post_id)
    email_author = post.author_post.user.email
    message = f'Hello,{instance.user}. Your comment" {instance.text}" on post was deleted by author {post.author_post}'
    send_mail(
        subject = 'Delete your comment',
        message = message,
        from_email = settings.DEFAULT_FROM_EMAIL,
        recipient_list = [email]
    )

@receiver(post_save,sender = Like)
def created_like(sender,instance,created,**kwargs):
    if created:
        author_like = instance.user
        author_comment = instance.comment.user
        email = author_comment.email
        send_mail(
            subject = 'Like on your comment!',
            message = f'User {author_like} has posted a like on your comment!',
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list = [email]
        )














"""
@receiver(user_signed_up,dispatch_uid = 'some.unique.string.id.for.allauth.user_signed_up')
def user_signed_up(request,user,**kwargs):
    send_mail(
        subject = 'Тестовое письмо',
        message = 'Потвердите регистрацию',
        from_email = 'sergeiazharkov@yandex.ru',
        recipient_list = ['agaverdyevsergej@gmail.com','agaverdyevaira@gmail.com']
    )
    redirect(to = 'categories/')
"""

