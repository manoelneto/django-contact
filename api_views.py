# -*- coding: utf-8 -*-
from rest_framework import viewsets, mixins
from .models import Contact
from .serializers import (
    ContactSerializer,
)


class ContactViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = ContactSerializer
    model = Contact
