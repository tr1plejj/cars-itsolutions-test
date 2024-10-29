from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView
from cars.forms import CarForm, CommentForm
from cars.models import Car, Comment


class CarListView(ListView):
    """Просмотр всех машин."""

    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'


class CarDetailWithCommentView(LoginRequiredMixin, View):
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