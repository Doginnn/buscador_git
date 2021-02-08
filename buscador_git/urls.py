from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from buscador_git.orgs.views import EmpresaViewSet

# End Points from API
api_router = routers.DefaultRouter()
api_router.register('', EmpresaViewSet),
api_router.register('orgs', EmpresaViewSet),


urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(api_router.urls)),
    path('orgs', include(api_router.urls)),
]
