from django.db import models


class Repo(models.Model):
    name = models.CharField(max_length=100)
    is_private = models.BooleanField(default=True)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def select_all_repos() -> list:
    repo_list = Repo.objects.all().values('name', 'is_private', 'owner')
    repo_info = [{'name': repo['name'], 'is_private': repo['is_private'], 'owner': repo['owner']} for repo in repo_list]
    return repo_info
