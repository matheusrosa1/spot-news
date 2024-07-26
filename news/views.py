from django.shortcuts import get_object_or_404, redirect, render

from news.forms import CategoryForm, NewsForm
from news.models import Category, News
from rest_framework import viewsets

from news.serializers import CategorySerializer


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def home_page(request):
    news_list = News.objects.all()
    return render(request, "home.html", {"news_list": news_list})


def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, "news_details.html", {"news": news})


def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    else:
        form = CategoryForm()

    return render(request, "categories_form.html", {"form": form})


def news_form(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news_instance = form.save(commit=False)
            categories = form.cleaned_data.get("categories")

            news_instance.save()

            if categories:
                news_instance.categories.set(categories)

            return redirect("home-page")
    else:
        form = NewsForm()

    return render(request, "news_form.html", {"form": form})
