from . import views
from django.urls import path
from insite import views


urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('post_detail/', views.PostDetail, name='post_detail'),
    path('contact/', views.contact, name='conatct'),
    path('exercise/', views.exercise, name='exercise'),
    path('health/', views.health, name='health'),
    path('mindfulness/', views.mindfulness, name='mindfulness'),
    path('wealth/', views.wealth, name='wealth'),
]
