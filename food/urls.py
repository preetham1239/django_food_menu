from django.urls import path
from . import views

"""
The following code is used to create the URL patterns for the food app. So, any URL for the below list should start with /food/. 
pk is the primary key of the food item. The primary key is the unique identifier for the food
"""
app_name = 'food'
urlpatterns = [
    path('', views.IndexClassListView.as_view(), name='index'),
    path('<int:pk>/', views.FoodItemDetailView.as_view(), name='detail'),
    path('add/', views.FoodItemCreateView.as_view(), name='create_item'),
    path('update/<int:pk>/', views.FoodItemUpdateView.as_view(), name='update_item'),
    path('delete/<int:pk>/', views.FoodItemDeleteView.as_view(), name='delete_item'),
]
