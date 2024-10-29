from cars.models import Car
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cars.api.serializers.car_serializer import CarSerializer


class CarView(generics.ListCreateAPIView):
    """Просмотр и создание машин."""

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр и удаление конкретной машины, изменение полей."""

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_update(self, serializer):
        car = self.get_object()
        if car.owner != self.request.user:  # Проверка, что пользователь является создателем
            raise PermissionDenied("У вас нет прав на изменение этого объекта.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:  # Проверка, что пользователь является создателем
            raise PermissionDenied("У вас нет прав на удаление этого объекта.")
        instance.delete()

