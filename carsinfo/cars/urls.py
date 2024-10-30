from django.urls import path, include
from cars.views.car_views import CarListView, CarCreateView, CarDetailWithCommentView, CarDeleteView, CarUpdateView
from cars.views.user_views import RegistrationView, UserProfileView


urlpatterns = [
    path('api/', include('cars.api.urls')),
    path('register/', RegistrationView.as_view(), name='register'),
    path('', CarListView.as_view(), name='index'),
    path('<int:pk>/', CarDetailWithCommentView.as_view(), name='car-detail'),
    path('create/', CarCreateView.as_view(), name='car-create'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('<int:pk>/edit/', CarUpdateView.as_view(), name='car-edit'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete')
]
