from django.urls import path
from .views import sign, BookList,BookDetail

app_name='test'
urlpatterns=[
    path('signup/',sign,name='register'),
    path('list/',BookList.as_view(),name='list'),
    path('list/<uuid:pk>/',BookDetail.as_view(),name='detail')
]