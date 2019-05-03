from django.urls import path
from .views import (
    #StatusListSearchAPIView,
    StatusAPIView,
    #StatusCreateAPIView,
    #StatusDetailAPIView,
    #StatusUpdateAPIView,
    #StatusDeleteAPIView,
    #StatusAPIDetailView
    )

urlpatterns = [
    #path('', StatusListSearchAPIView.as_view()),
    path('', StatusAPIView.as_view()),
    #path('create/', StatusCreateAPIView.as_view()),
    #path('<int:pk>/', StatusAPIDetailView.as_view()),
    #path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
    #path('<int:pk>/delete/', StatusDeleteAPIView.as_view()),
]
