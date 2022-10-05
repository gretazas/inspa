from django.urls import path
from insite import views


urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('posts/', views.PostsList.as_view(), name='posts'),
    path('contact/', views.contact, name='conatct'),
    path('exercise/', views.ExercisePostsList.as_view(), name='exercise'),
    path('health/', views.HealthPostsList.as_view(), name='health'),
    path('mindfulness/', views.MindfulnessPostsList.as_view(), name='mindfulness'),
    path('wealth/', views.WealthPostsList.as_view(), name='wealth'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
