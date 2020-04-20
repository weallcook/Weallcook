from django.shortcuts import render
from .models import Article
# Create your views here.

def blog_index(request):
	articles = Article.objects.all()
	data = {'articles': articles}
	return render(request, 'blog/blog_index.html',data)



def article(request,name):
	try : 
		article = Article.objects.get(title=name)
		data = { 'article': article}
	except :
		data = {'message' : 'l\'article que vous avez demandé n\' existe pas '}
	return render(request, 'blog/article.html',data)