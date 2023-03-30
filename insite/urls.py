from django.urls import path
from insite import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('team/', views.Team.as_view(), name='team'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('add_post/', views.Addpost.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('posts/<post_type>/', views.PostsList.as_view(), name='posts'),
]
