from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm
from .models import Product, Category
from .filters import ProductFilter


class ProductList(ListView):
    model = Product
    ordering = 'product_name'
    template_name = 'products.html'
    paginate_by = 2
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['time'] = datetime.utcnow
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    model = Product
    template_name = 'product_edit.html'
    form_class = ProductForm


class ProductEdit(UpdateView, LoginRequiredMixin):
    model = Product
    template_name = 'product_edit.html'
    form_class = ProductForm


class ProductDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('app.delete_product',)
    model = Product
    template_name = 'product_delete.html'
    form_class = ProductForm
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(pk=pk)
    category.subscribers.add(user)
    return redirect('category_list')


@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(pk=pk)
    category.subscribers.remove(user)
    return redirect('category_list')

