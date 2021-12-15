from django.urls import path

from admins.views import index, \
    admin_product, UserListView, UserCreateView, UserUpdateView, UserDeleteView, admin_category_create, admin_category

app_name = 'admins'
urlpatterns = [

    path('', index,name='index'),

    path('users/', UserListView.as_view(),name='admin_users'),
    path('users-create/', UserCreateView.as_view(),name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(),name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(),name='admin_users_delete'),

    path('category/create/', admin_category_create, name='admin_category_create'),
    path('category/', admin_category, name='admin_category'),
    path('products/', admin_product, name='admin_product'),

]