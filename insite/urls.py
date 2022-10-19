from django.urls import path
from insite import views


urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('posts/<post_type>/', views.PostsList.as_view(), name='posts'),
    path('add_post/', views.Addpost.as_view(), name='add_post'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
