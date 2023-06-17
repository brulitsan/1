from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.mixins import LoginRequiredMixin
from avtosalon.models import Buyer
from avtosalon.permissions import IsOwnerOrReadOnly, IsAdminReadOnly, ManagerOnly
from avtosalon.serializesr import AutosalonSerializer


class AutosalonViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   LoginRequiredMixin,
                   GenericViewSet):

    queryset = Buyer.objects.all()
    serializer_class = AutosalonSerializer
    permission_classes = (ManagerOnly, )


