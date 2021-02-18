from django.shortcuts import render, get_object_or_404

from main import models
# Create your views here.
def index(request):
    #adding '\' to join the commands in next line. It's same as models.Article.object.all().order_by('-createdAt)[:10]
    latest_articles = models.Article.objects \
    .all() \
    .order_by('-createdAt')[:10]
    context={
        'latest_articles':latest_articles
    }
    response = render(request, 'main/index.html', context)
    return response

def article(request, pk):
    #this get_object_or_404 class Works as an alternative for models.Article.object.get(id=pk) 
    # and even thrown an 404 EXCEPTION in case any
    article = get_object_or_404(models.Article, pk=pk) #pk =pk is same as id =pk but the diff is that it can even
    #accept the primary key created by us.

    context ={
        'article':article
    }
    response = render(request, 'main/article.html', context)
    return response

def author(request, pk):
    author = get_object_or_404(models.Author, pk=pk)

    context = {
        'author':author
    }
    return render(request, 'main/author.html', context)

def create_article(request):

    authors = models.Author.objects.all()
    context = {
        'authors':authors
    }

    if request.method =="POST":
        article_data = {
            'title':request.POST['Title'],
            'content':request.POST['content']
        }
        article = models.Article.objects.create(**article_data)
        author = models.Author.objects.filter(pk = request.POST['author'])
        article.authors.set(author)
        #now if data is received successfully
        context["success"] = True  #we will use this in our html doc
    
    return render(request, 'main/create_article.html', context)
