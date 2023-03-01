from django.urls import path

from .views import UsersView, UserView


urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('<int:pk>/', UserView.as_view(), name='user_details'),
]