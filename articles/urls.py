from django.contrib import admin
from django.urls import path
from . import views
app_name = "articles"

urlpatterns = [
    path('dashboard/', views.dashboard , name = "dashboard"),
    path('addarticle/', views.addArticle , name = "addArticle"),
    path('delete/<int:id>', views.deleteArticle , name = "deleteArticle"),
    path('update/<int:id>', views.updateArticle , name = "updateArticle"),
    path('article/<int:id>', views.seeArticle , name = "seeArticle"),
    path('', views.seeAllArticles , name = "seeAllArticles"),
    path('comment/<int:id>', views.addComment , name = "comment"),
]