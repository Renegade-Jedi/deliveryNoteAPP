from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Document
from documentProcessing import serializers

class DocumentViewSet(viewsets.ModelViewSet):
    """View for manage document api"""
    serializer_class = serializers.DocumentSerializer
    queryset = Document.objects.all()



