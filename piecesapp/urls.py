
from django.urls import  include, path 
from rest_framework import routers 
from . import views 

router = routers.DefaultRouter()


#router.register(r'board', views.BoardViewSet)
#router.register(r'pieces', views.PiecesAPIView, basename='pieces')
urlpatterns = [
    path('pieces/', views.PiecesAPIView.as_view(),name='pieces'),
    path('board/', views.BoardAPIView.as_view(),name='board'),
]+ router.urls

