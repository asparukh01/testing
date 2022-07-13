from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    CreateEmployeeView,
    ListEmployeeView,
    DetailEmployeeView,
    DeleteEmployeeView,
    UpdateEmployeeView, LogoutView, )


urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_token_delete'),
    path('create_employee/', CreateEmployeeView.as_view(), name='create_employee'),
    path('detail_employee/<int:pk>/', DetailEmployeeView.as_view(), name='detail_employee'),
    path('delete_employee/<int:pk>/', DeleteEmployeeView.as_view(), name='delete_employee'),
    path('update_employee/<int:pk>/', UpdateEmployeeView.as_view(), name='update_employee'),
    path('', ListEmployeeView.as_view(), name='list_employee'),
]
