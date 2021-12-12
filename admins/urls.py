from django.urls import path

from admins.views import index, admin_users_create, admin_users_update, admin_users_delete, admin_users, admin_category, admin_product,admin_category_create

app_name = 'admins'
urlpatterns = [

    path('', index,name='index'),

    path('users/', admin_users,name='admin_users'),
    path('users-create/', admin_users_create,name='admin_users_create'),
    path('users-update/<int:pk>', admin_users_update,name='admin_users_update'),
    path('users-delete/<int:pk>', admin_users_delete,name='admin_users_delete'),

    path('category/create/', admin_category_create, name='admin_category_create'),
    path('category/', admin_category, name='admin_category'),
    path('products/', admin_product, name='admin_product'),

]