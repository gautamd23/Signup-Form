from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView,TokenRefreshView
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='home'),
    path('logout/',views.user_logout, name='logout'),
    path('registration/',views.registration, name= 'reg'),
    path('login/', views.user_login,name='login'),
    path('detail/', views.detail,name='detail'),
    path('delete/<int:id>/', views.delete, name='deleted'),
    path('<int:id>/', views.update, name='updated'),
    path('gettoken/',TokenObtainPairView.as_view(), name ="token_ob_pair"),
    path('reftoken/',TokenRefreshView.as_view(), name ="token_ob_pair"),
    path('vertoken/',TokenVerifyView.as_view(), name ="token_ob_pair"),
    # path('login/', LoginView, name='customlogin'),



]