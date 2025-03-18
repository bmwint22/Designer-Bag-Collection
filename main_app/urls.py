from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='home'),  
    path('landing/', views.landing, name='landing'),  
    path('bags/', views.bag_index, name='bag-index'),
    path('bags/<int:bag_id>/', views.bag_detail, name='bag-detail'),
    path('bags/create/', views.BagCreate.as_view(), name='bag-create'),
    path('bags/<int:pk>/update/', views.BagUpdate.as_view(), name='bag-update'),
    path('bags/<int:pk>/delete/', views.BagDelete.as_view(), name='bag-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
]
