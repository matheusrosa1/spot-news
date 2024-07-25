from django.shortcuts import get_object_or_404, render

from news.models import News

# Create your views here.


def home_page(request):
    news_list = News.objects.all()
    return render(request, "home.html", {"news_list": news_list})


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, "news_detail.html", {"news": news})
