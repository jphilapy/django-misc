from django.urls import path
from .views import HomePageView, AboutPageView, TestVarPageView, ListPageView, DetailPageView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("test_var/", TestVarPageView.as_view(), name="test_var"),
    path("list/", ListPageView.as_view(), name="list"),
    path("detail/<int:id>", DetailPageView.as_view(), name="detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)