from django.urls import path
from todo.api import views as api_views
from . import views

app_name = 'todo'
urlpatterns = [
    path('list/', views.TodoListView.as_view(), name='list_view'),
    path('create/', views.TodoCreateView.as_view(), name='create_view'),
    path('<uuid:uuid>/update/', views.TodoUpdateView.as_view(), name='update_view'),
    path('<uuid:uuid>/delete/', views.TodoDeleteView.as_view(), name='delete_view'),
    path('<uuid:uuid>/detail/', views.TodoDetailView.as_view(), name='detail_view'),
    # api views
    path('api/', api_views.TodoListCreateAPIView.as_view()),
    path('api/<uuid:uuid>/', api_views.TodoRetriveUpdateDestroyAPIView.as_view()),
]