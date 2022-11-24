from django.urls import (
    path,include
)

from rest_framework.routers import DefaultRouter
from documentProcessing import views

router = DefaultRouter()
router.register('document', views.DocumentViewSet)
app_name = 'document'

urlpatterns = [
    path('', include(router.urls)),
]
