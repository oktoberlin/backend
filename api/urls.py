from django.urls import path
from . import views
from .views import UserRecordView
urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/create/', views.createNote),
    path('notes/<str:pk>/update/', views.updateNote),
    path('notes/<str:pk>/delete/', views.deleteNote),
    path('notes/<str:pk>/', views.getNote),
    path('user/', UserRecordView.as_view(), name='users'),
]