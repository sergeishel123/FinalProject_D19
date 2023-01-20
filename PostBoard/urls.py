from django.urls import path
from .views import PostLists,PostDetail,PostCreate,PostUpdate,all_categories,PersonalView,CommentDetail,CommentDelete,like_create,CommentList

urlpatterns = [
    path('',PostLists.as_view(),name = 'post_lists'),
    path('<int:pk>',PostDetail.as_view(),name = 'post_detail'),
    path('create', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update',PostUpdate.as_view(),name = 'post_update'),
    path('categories/',all_categories,name = 'all_categories'),
    path('personal/',PersonalView.as_view(),name = 'personal'),
    path('personal/comments/',CommentList.as_view(),name = 'all_comments'),
    path('personal/comments/<int:pk>',CommentDetail.as_view(),name = 'comment_detail'),
    path('personal/comments/<int:pk>/delete/',CommentDelete.as_view(),name = 'comment_delete'),
    path('personal/comments/<int:pk>/like',like_create,name = 'like_create')

]