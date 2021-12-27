from django.urls import path

from .views import RepoListView, all_added_repos

app_name = 'repos'

urlpatterns = [
    path('', RepoListView.as_view(), name='repo_list'),
    path('getRepos/', all_added_repos),
]
