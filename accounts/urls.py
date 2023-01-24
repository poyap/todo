from django.urls import path
from .views import UserRegisterView, UserUpdateView, UserDetailView, UserDeleteView
from api import views as api_views

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'account_register'),
    path('update/', UserUpdateView.as_view(), name='account_update'),
    path('detail/', UserDetailView.as_view(), name='account_detail'),
    path('delete/', UserDeleteView.as_view(), name='account_delete'),
    # api view
    path('api/', api_views.UserListCreateAPIView.as_view(), name= 'account_rest_list'),
    path('api/<int:pk>', api_views.UserRetriveUpdateDestroyAPIView.as_view(), name= 'account_rest_update'),
]