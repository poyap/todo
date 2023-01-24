from django.urls import path
from . import views
from api import views as api_views

app_name = 'todo'

urlpatterns = [
    path('list/', views.TodoListView.as_view(), name='list_view'),
    path('create/', views.TodoCreateView.as_view(), name='create_view'),
    path('<int:pk>/update', views.TodoUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete', views.TodoDeleteView.as_view(), name='delete_view'),
    path('<int:pk>/detail', views.TodoDetailView.as_view(), name='detail_view'),
    # api views
    path('api/', api_views.TodoListCreateAPIView.as_view(), name='list_rest_api'),
    path('api/<int:pk>', api_views.TodoRetriveUpdateDestroyAPIView.as_view(), name='update_rest_api'),
]