from django.urls import path

from news.views import category_form, home_page, news_detail, news_form


urlpatterns = [
    path("", home_page, name="home-page"),
    path("news/<int:id>", news_detail, name="news-details-page"),
    path("categories", category_form, name="categories-form"),
    path("news", news_form, name="news-form"),
]
