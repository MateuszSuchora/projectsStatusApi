import json

from django.http import HttpResponse
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
        results_to_template = {'repos_list': repos, 'count': len(repos)}
        return HttpResponse(json.dumps(results_to_template), content_type="application/json")
    except:
        response_data = {'result': 'error'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
