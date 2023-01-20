from django.urls import path,include
from .views import protect_view,login_view,code_auth
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',protect_view,name = 'protect_view'),
    path('login/',login_view,name = 'login'),
    path('code/(?P<user_id>\d+)',code_auth,name= 'auth_code'),
    path('logout/',LogoutView.as_view(template_name = 'protect/logout.html'),name = 'logout'),
]