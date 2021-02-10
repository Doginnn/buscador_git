from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from buscador_git.orgs.views import OrgViewSet, GitViewSet

# End Points from API
router = DefaultRouter()
router.register('', OrgViewSet),
router.register('orgs', GitViewSet),


urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
    path('orgs', include(router.urls)),
]
