from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
import pdb
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DetailView,
)
# Create your views here.


from .models import Article
from .forms import ArticleModelForm


class ArticleListView(ListView):
    template_name = "article_list.html"
    queryset = Article.objects.all()

class ArticleCreateView(CreateView):
    model = Article
    queryset = Article.objects.all()
    form_class = ArticleModelForm
    template_name = "article_create.html"
    
    def post (self, request, *args, **kwargs):
        form = self.get_form()
        self.object = form.save()
        return redirect("blog:article-list")

    
    def form_valid(self, form):
        print(form.clean)
        print("--------")
        super().form_valid(form)
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")  #can also print this to get all dict values
        return get_object_or_404(Article,id=id_)