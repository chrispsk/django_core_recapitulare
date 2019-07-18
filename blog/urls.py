from django.urls import path
from .views import post_model_list_view1, search, delete_view, post_model_list_view2, detail_view, create_view, update_view

urlpatterns = [
    path('', post_model_list_view1, name='list1'),
    path('s/', post_model_list_view2, name='list2'),
    path('<int:id>/', detail_view, name='detail'),
    path('c/', create_view, name='create'),
    path('<int:id>/edit/', update_view, name='update'),
    path('<int:id>/delete/', delete_view, name='delete'),
    path('search/', search, name='search'),
]
