from django.urls import path
from . import views


urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),



#    path('', views.home, name='home'),
    path('', views.index, name='index'),
#    path('', views.get_name, name='get_name'),
    path('travelr',views.get_travelr),

]
