from django.urls import include, path

from news.views import (
    CategoryViewSet,
    category_form,
    home_page,
    news_detail,
    news_form,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    path("", home_page, name="home-page"),
    path("api/", include(router.urls)),
    path("news/<int:id>", news_detail, name="news-details-page"),
    path("categories", category_form, name="categories-form"),
    path("news", news_form, name="news-form"),
]
