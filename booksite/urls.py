"""
URL configuration for booksite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.views import (
    BookViewSet,
    FictionViewSet,
    FantasyViewSet,
    MysteryViewSet,
    RomanceViewSet,
    HorrorViewSet,
    ScienceFictionViewSet,
    BiographyViewSet,
    HistoryViewSet,
    PoetryViewSet,
    KidsViewSet,
)
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('books', BookViewSet, basename='book')
router.register('fiction', FictionViewSet, basename='fiction')
router.register('fantasy', FantasyViewSet, basename='fantasy')
router.register('mystery', MysteryViewSet, basename='mystery')
router.register('romance', RomanceViewSet, basename='romance')
router.register('horror', HorrorViewSet, basename='horror')
router.register('sci-fi', ScienceFictionViewSet, basename='sci-fi')
router.register('biography', BiographyViewSet, basename='biography')
router.register('history', HistoryViewSet, basename='history')
router.register('poetry', PoetryViewSet, basename='poetry')
router.register('kids', KidsViewSet, basename='kids')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)