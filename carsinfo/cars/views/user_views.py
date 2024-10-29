from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from cars.forms import RegistrationForm
from cars.models import Car

User = get_user_model()


class RegistrationView(CreateView):
    """Регистрация пользователя."""

    template_name = 'cars/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


class UserProfileView(LoginRequiredMixin, DetailView):
    """Отображение профиля пользователя."""

    model = User
    template_name = 'cars/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        # Получаем контекст от родительского метода
        context = super().get_context_data(**kwargs)

        # Добавляем все автомобили, принадлежащие текущему пользователю
        context['user_cars'] = Car.objects.filter(owner=self.request.user)

        return context