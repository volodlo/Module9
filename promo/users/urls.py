from django.urls import path
from .views import SignUpView, profile, UserUpdateView, LoginUser, password

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/<int:current_user>/', profile, name='profile'),
    path('edit_profile/<int:pk>/', UserUpdateView.as_view(), name='edit_profile'),
    path('edit_profile/password/', password, name='password'),

]
