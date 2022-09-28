from . import views
from django.urls import path
from insite.views import contact


urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('contact/', contact, name='conatct'),
]
