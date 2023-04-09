from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    path('', views.IndexClassListView.as_view(), name='index'),
    path('<int:pk>/', views.FoodItemDetailView.as_view(), name='detail'),
    path('fooditem/', views.items, name='items'),
    path('add/', views.create_item, name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
