from django.urls import path
from cars.api.views.car_view import CarView, CarDetailView
from cars.api.views.comment_view import CommentView
from rest_framework.authtoken import views
from cars.api.views.user_view import UserRegistrationView


urlpatterns = [
    path('cars/', CarView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('cars/<int:pk>/comments/', CommentView.as_view(), name='comment-list'),
    path('token/', views.obtain_auth_token, name='token'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]