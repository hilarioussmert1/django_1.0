from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductEdit, ProductDelete, CategoryListView, subscribe, \
    unsubscribe

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductEdit.as_view(), name='product_edit'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),
]
