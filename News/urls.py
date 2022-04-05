from django.urls import path
from .views import *


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('create/', PostCreate.as_view()),
    path('search/', SearchList.as_view()),
    path('delete/<int:pk>', PostDelete.as_view()),
    path('update/<int:pk>',PostUpdate.as_view()),
]