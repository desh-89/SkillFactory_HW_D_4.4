from django.urls import path
from .views import *


urlpatterns = [
    path('news', PostList.as_view()),
    path('new/<int:pk>/', PostDetail.as_view())
]
