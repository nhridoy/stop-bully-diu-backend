from django.urls import path
from e_shop import views as e_view

urlpatterns = [
    path('products/', e_view.ProductsView.as_view(), name='product_add_and_list'),
]
