from django.views.generic import ListView
from .models import Repo


class RepoListView(ListView):
    model = Repo
