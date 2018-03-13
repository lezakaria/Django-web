from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Articles
from .forms import PostForm
from django.core.urlresolvers import reverse
# Create your views here.

def about(request):
    return render(request, 'articles/about.html')



def articles_list(request):
    articles_list = Articles.objects.all().order_by('created_at')
    context = {'articles': articles_list}
    return render(request, 'articles/ListArticles.html', context)

def article_detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/blog.html', context)

#def article_detail(request, pk):
#    article = Articles.objects.get(pk=pk)
#    context = {'article': article}
#    return render(request, 'articles/DetailArticle.html', context)

def article_edit(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    form = PostForm(request.POST, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.updated_at = timezone.now()
        article.save()
      #  message = "Article succesfully updated at " + article.updated_at.strftime('%Y-%m-%d %H:%M:%S')
       # context = {"message": message , "form": form}
        return redirect('articles:articles_list')
    else:
        form = PostForm(instance=article)
       # context = {"message": "", "form": form}
    return render(request, 'articles/EditArticle.html', context)

def delete(request, pk):
        article=get_object_or_404(Articles, pk=pk).delete()
       # return render(request, "articles/delete.html")
        return render(request,'articles/delete.html')

def create_articles(request):
   
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date =timezone.now()
            article.save()
              
        return redirect('articles:articles_list')
    else:
        form = PostForm()
    return render(request, 'articles/createArticles.html', {'form': form})
