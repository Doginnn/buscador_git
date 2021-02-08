from rest_framework import viewsets
from buscador_git.orgs.serializers import EmpresaSerializer
from buscador_git.orgs.models import Empresa


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()
