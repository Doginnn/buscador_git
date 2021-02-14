from django.shortcuts import render
from rest_framework import viewsets
from buscador_git.orgs.serializers import OrgSerializer
from buscador_git.orgs.models import Org
from github import Github, GithubException
from decouple import config
import requests


# class OrgView(viewsets.ModelViewSet):
#     queryset = Org.objects.all()
#     serializer_class = OrgSerializer

def github_org(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    return render(request, 'github.html', {'search_result': search_result})


# GET Org - ['name','slug']
def github_client(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        client = Github()

        try:
            user = client.get_user(username)
            search_result['name'] = user.name
            search_result['login'] = user.login
            search_result['public_repos'] = user.public_repos
            search_result['success'] = True
        except GithubException as ge:
            search_result['message'] = ge.data['message']
            search_result['success'] = False

    return render(request, 'github.html', {'search_result': search_result})


# GET ListOrg
def github_list_org(request):
    pass


# GET ListRepoOrg
def github_repo_org(request):
    pass


# GET ListPopularityEmpresa
def github_popularity_org(request):
    pass
