from contextlib import redirect_stderr
from operator import getitem
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Article,Comment
from .forms import articleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
#Home Page
def index(request):
    return render(request,"index.html")

#About Me Page
def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def addArticle(request):
    form = articleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article Successfully Added")
        return redirect("index")
    return render(request,"addArticle.html",{"form" : form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,'Article Successfully Deleted')
    return redirect('articles:dashboard')

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = articleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article Successfully Updated")
        return redirect("articles:dashboard")
    return render(request,'updateArticle.html',{'form' : form})

@login_required(login_url="user:login")
def seeArticle(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all()
    return render(request,"seeArticle.html",{"article" : article,"comments":comments})

@login_required(login_url="user:login")
def seeAllArticles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"allArticles.html",{"articles" : articles})
    articles = Article.objects.all()
    return render(request,"allArticles.html",{"articles" : articles})

def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    
    if request.method == 'POST':
        commentAuthor = request.POST.get('commentAuthor')
        commentContent = request.POST.get('commentContent')
        newComment = Comment(commentAuthor = commentAuthor,commentContent = commentContent)
        newComment.article = article
        newComment.save()
    return redirect(reverse('articles:seeArticle',kwargs={'id':id}))
