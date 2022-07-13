from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Employee
from .serializer import EmployeeSerializer


class CreateEmployeeView(GenericAPIView):
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        serializer = EmployeeSerializer()
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ListEmployeeView(ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'post', 'salary', 'boss', 'adopted_to_job']
    search_fields = ['name', 'post']
    queryset = Employee.objects.all()


class DetailEmployeeView(GenericAPIView):
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        objects = get_object_or_404(Employee, pk=kwargs.get('pk'))
        serializer = self.serializer_class(objects)
        return Response(serializer.data)


class DeleteEmployeeView(GenericAPIView):
    def delete(self, request, *args, **kwargs):
        objects = get_object_or_404(Employee, pk=kwargs.get('pk'))
        objects.delete()
        return Response({"status": "success", "data": objects.pk})


class UpdateEmployeeView(GenericAPIView):
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        objects = get_object_or_404(Employee, pk=kwargs.get('pk'))
        serializer = self.serializer_class(objects)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        objects = get_object_or_404(Employee, pk=kwargs.get('pk'))
        serializer = self.serializer_class(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})
