from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,TemplateView,DeleteView
from .models import Post,Category,Author,PostCategory,Comment,Like
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .filters import CommentFilter

# Create your views here.

class PostLists(LoginRequiredMixin,ListView):
    model = Post

    template_name = 'post_list.html'

    ordering = 'time_in'

    context_object_name = 'posts'

    paginate_by = 2

class PostDetail(LoginRequiredMixin,DetailView,):
    model = Post

    template_name = 'post_detail.html'

    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categor'] = PostCategory.objects.get(post = self.object).category
        return context

    def post(self,request,pk,*args,**kwargs):
        comment_text = request.POST['comment_text']
        user = request.user
        post = Post(id = pk)
        Comment.objects.create(post = post,user = user,text = comment_text)
        return redirect('post_detail',pk = pk)


class PostCreate(LoginRequiredMixin,CreateView):
    model = Post

    template_name = 'post_create.html'

    form_class = PostForm

    def post(self,request,*args,**kwargs):
        post = self.request.POST
        author_post,heading,text,category,cover = request.user.id,post['heading'],post['text'],post['category'],post.get('cover',)
        print(11111111111111111111111,cover)
        New = Post(author_post = Author.objects.get(user = author_post),heading = heading, text = text,cover = cover)
        New.save()
        Categor = Category.objects.get(name = category)
        PostCategory.objects.create(post = New,category = Categor)
        return redirect(New.get_absolute_url())


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post

    template_name = 'post_edit.html'

    form_class = PostForm


@login_required
def all_categories(request):
    context = {}
    context['categories'] = Category.objects.all()
    return render(request,'categories.html',context)


class PersonalView(LoginRequiredMixin,TemplateView):
    template_name = 'protect/personal.html'
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post__author_post__user = self.request.user)[:3]
        return context

class CommentList(ListView):
    model = Comment
    template_name = 'protect/comment_list_all.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CommentFilter(self.request.GET,queryset)
        return self.filterset.qs

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['comments'] = Comment.objects.filter(post__author_post__user = self.request.user)
        return context

class CommentDetail(LoginRequiredMixin,DetailView):
    model =Comment
    template_name = 'protect/comment_detail.html'
    context_object_name = 'comment'



    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_like'] = not Like.objects.filter(user = self.request.user, comment = self.object).exists()
        return context

class CommentDelete(LoginRequiredMixin,DeleteView):
    model = Comment
    template_name = 'protect/comment_delete.html'
    success_url = reverse_lazy('personal')
    context_object_name = 'comment'



def like_create(request,pk):
    like_user_id = request.user.id
    comment_id = pk
    Like.objects.create(user_id = like_user_id,comment_id = pk)
    return redirect(to = 'comment_detail',pk = comment_id)


