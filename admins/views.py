

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryUpdateFormAdmin
from authapp.models import User


# Create your views here.
from mainapp.models import Products, ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Регистрация',
        'form': form
    }
    return render(request,'admins/admin-users-create.html',context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, pk):

    user_select = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST,instance=user_select,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'user_select':user_select
    }


    return render(request, 'admins/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request,pk):

    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.is_active=False
        user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))

def admin_category(request):
    context = {
        "categories": ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-category-read.html', context)


def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryUpdateFormAdmin(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category_read'))
    else:
        form = CategoryUpdateFormAdmin()
    context = {
        'title': 'Geekshop - Админ | Правка',
        'form': form
    }
    return render(request,'admins/admin_category_create.html',context)


def admin_product(request):
    context = {
        "products": Products.objects.all()
    }
    return render(request, 'admins/admin-product-read.html', context)



