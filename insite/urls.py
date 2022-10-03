from . import views
from django.urls import path
from insite import views


urlpatterns = [
    path('', views.homePage.as_view(), name="home"),
    path('posts/', views.AllPostsList.as_view(), name='posts'),
    path('contact/', views.contact, name='conatct'),
    path('exercise/', views.exercise, name='exercise'),
    path('health/', views.health, name='health'),
    path('mindfulness/', views.mindfulness, name='mindfulness'),
    path('wealth/', views.wealth, name='wealth'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
