from django.views import generic
from sales.models import Sales


class GitLearning(generic.list):
    model = Sales
    template_name = 'sales/main.html'
    context_object_name = 'qs'
