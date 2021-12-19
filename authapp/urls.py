from django.urls import path
# from authapp.views import
from authapp.views import RegisterListView, LoginListView, ProfileFormView, Logout

app_name = 'authapp'
urlpatterns = [

    path('login/', LoginListView.as_view(), name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileFormView.as_view(), name='profile'),

]
