from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path('authenticate/', views.authenticate_user, name='authenticate_user'),
    path('follow/<int:id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:id>/', views.unfollow_user, name='unfollow_user'),
    path('user/', views.get_user_profile, name='get_user_profile'),
    path('posts/', views.create_post, name='create_post'),
    path('posts/<int:id>/', views.delete_post, name='delete_post'),
    path('like/<int:id>/', views.like_post, name='like_post'),
    path('unlike/<int:id>/', views.unlike_post, name='unlike_post'),
    path('comment/<int:id>/', views.add_comment, name='add_comment'),
    path('posts/<int:id>/', views.get_post_detail, name='get_post_detail'),
    path('all_posts/', views.get_all_posts, name='get_all_posts'),
    # Add more paths for other views as needed...
]
