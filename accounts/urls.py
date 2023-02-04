from django.urls import path

from .views import SignUpView, UserView


urlpatterns = [
    path('', UserView.as_view(), name='users'),
    path('signup/', SignUpView.as_view(), name='signup'),
]