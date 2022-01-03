from django.urls import path

from admins.views import index, \
    UserListView, UserCreateView, UserUpdateView, UserDeleteView, \
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, ProductListView, ProductCreateView

app_name = 'admins'





urlpatterns = [

    path('', index,name='index'),

    path('users/', UserListView.as_view(),name='admin_users'),
    path('users-create/', UserCreateView.as_view(),name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(),name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(),name='admin_users_delete'),

    path('category-create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category/', CategoryListView.as_view(), name='admin_category'),
    path('category-update/<int:pk>', CategoryUpdateView.as_view(),name='admin_category_update'),
    path('category-delete/<int:pk>', CategoryDeleteView.as_view(),name='admin_category_delete'),

    path('products/', ProductListView.as_view(), name='admin_product'),
    path('products-create/', ProductCreateView.as_view(), name='admin_product_create'),
]