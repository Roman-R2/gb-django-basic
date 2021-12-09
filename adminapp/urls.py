from django.urls import path

from adminapp.views import users, user_create, user_update, user_delete, \
    categories, category_create, category_update, category_delete, products,\
    product_create, product_update, product_delete

app_name = 'adminapp'

urlpatterns = [
    path('users/', users, name='users'),
    path('user/create/', user_create, name='user_create'),
    path('user/update/<int:pk>/', user_update, name='user_update'),
    path('user/delete/<int:pk>/', user_delete, name='user_delete'),

    path('categories/', categories, name='categories'),
    path('category/create/', category_create, name='category_create'),
    path('category/update/<int:pk>/', category_update, name='category_update'),
    path('category/delete/<int:pk>/', category_delete, name='category_delete'),

    path('products/<int:pk>/', categories, name='categories'),
    path('products/create/', product_create, name='product_create'),
    path('products/update/<int:pk>/', product_update, name='product_update'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),

]
