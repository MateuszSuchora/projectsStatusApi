from django.urls import path

from .views import RepoListView

app_name = 'repos'

urlpatterns = [
    path('', RepoListView.as_view(), name='repo_list'),
]
