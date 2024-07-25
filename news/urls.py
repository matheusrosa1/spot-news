from django.urls import path

from news.views import home_page, news_detail


urlpatterns = [
    path("", home_page, name="home-page"),
    path("news/<int:news_id>", news_detail, name="news-detail"),
]
