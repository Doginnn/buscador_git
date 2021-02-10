from rest_framework import viewsets
from buscador_git.orgs.serializers import OrgSerializer
from buscador_git.orgs.models import Org
from github import Github

ACCESS_TOKEN = '21838791231789ecbc4b3de3576e2ba549b66550'
g = Github(ACCESS_TOKEN)


class OrgViewSet(viewsets.ModelViewSet):
    serializer_class = OrgSerializer
    queryset = Org.objects.all()

    def search_github():
        print()
    search_github()
