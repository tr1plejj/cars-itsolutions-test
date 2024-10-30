from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from cars.forms import CarForm, CommentForm
from cars.models import Car, Comment
from django.http import HttpResponseForbidden


class CarListView(ListView):
    """Просмотр всех машин."""

    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'


class CarDetailWithCommentView(View):
    """Просмотр конкретной машины, комментариев к ней и создание комментария."""

    template_name = 'cars/car_detail.html'

    def get(self, request, pk, *args, **kwargs):
        car = get_object_or_404(Car, pk=pk)
        comments = Comment.objects.filter(car=car)
        form = CommentForm()

        context = {
            'car': car,
            'comments': comments,
            'form': form,
        }

        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request, pk, *args, **kwargs):
        car = get_object_or_404(Car, pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            form.instance.car = car
            form.instance.author = request.user
            form.save()
            return self.get(request, pk)

        comments = Comment.objects.filter(car=car)
        context = {
            'car': car,
            'comments': comments,
            'form': form,
        }

        return render(request, self.template_name, context)


class CarCreateView(LoginRequiredMixin, CreateView):
    """Создание машины (только авторизованным)."""

    template_name = 'cars/create_car.html'
    form_class = CarForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car-detail', kwargs={'pk': self.object.pk})


class CarDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление автомобиля."""

    model = Car
    template_name = 'cars/delete_car.html'
    success_url = reverse_lazy('user-profile')

    def dispatch(self, request, *args, **kwargs):
        # Получаем объект
        self.object = self.get_object()
        # Проверяем, является ли текущий пользователь создателем объекта
        if self.object.owner != request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет прав для удаления этого объекта.")


class CarUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование автомобиля."""

    form_class = CarForm
    model = Car
    template_name = 'cars/update_car.html'

    def dispatch(self, request, *args, **kwargs):
        # Получаем объект
        self.object = self.get_object()
        # Проверяем, является ли текущий пользователь создателем объекта
        if self.object.owner != request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет прав для изменения этого объекта.")

    def get_success_url(self):
        return reverse('car-detail', kwargs={'pk': self.object.pk})

