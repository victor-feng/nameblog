from django.shortcuts import render

# Create your views here.
from blog.models import Article,Tag,Classification
from django.template import RequestContext

def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    return render(request,'index.html',{'blogs':blogs})
