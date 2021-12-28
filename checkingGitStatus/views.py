import json

from allauth.socialaccount.models import SocialToken
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from .models import Repo, select_all_repos
from rest_framework.decorators import api_view


class RepoListView(ListView):
    model = Repo


@csrf_exempt
@api_view(['POST'])
def all_added_repos(request):
    try:
        repos = select_all_repos()
        user = request.user
        result = SocialToken.objects.filter(account__user=user)
        results_to_template = {'repos_list': repos, 'count': len(repos), 'token': str(result[0])}
        return HttpResponse(json.dumps(results_to_template), content_type="application/json")
    except:
        response_data = {'result': 'error'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def add_repo(request):  # main/basic page
    return render(request, 'add_repo.html')


@csrf_exempt
@api_view(['POST'])
def add_repo_from_request(request):
    try:
        if request.method == "GET":
            response_data = {'result': 'wrong request'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        if request.method == "POST":
            json_data = request.data
            name = json_data["name"]
            is_private = json_data["is_private"]
            owner = json_data["owner"]
            Repo.objects.create(name=name, is_private=is_private, owner=owner)
            response_data = {'result': 'repo added'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    except:
        raise
        response_data = {'result': 'error'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
