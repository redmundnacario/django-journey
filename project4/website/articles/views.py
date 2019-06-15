from django.views.generic import ListView, DeleteView
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'article'

class ArticleDetailView(DeleteView):
    model = Article
    template_name = 'details.html'
    context_object_name = 'article'