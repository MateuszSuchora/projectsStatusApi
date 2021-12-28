from django.urls import path
from checkingGitStatus.views import RepoListView, all_added_repos, add_repo, add_repo_from_request

app_name = 'repos'

urlpatterns = [
    path('', RepoListView.as_view(), name='repo_list'),
    path('getRepos/', all_added_repos),
    path('repos/add/', add_repo),
    path('repos/add/addRepo/', add_repo_from_request),

]
