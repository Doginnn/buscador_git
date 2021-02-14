from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .orgs import views

# End Points from API
# router = SimpleRouter()
# router.register('', OrgView),
# router.register('orgs', views.github_org),


urlpatterns = [
    path('admin', admin.site.urls),
    # path('', include(router.urls)),
    # path('orgs', include(router.urls)),
    path('github', views.github_org),
    path('github/client/', views.github_client),
]
