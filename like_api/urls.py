"""like_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from api.views import news, category, journey, comment
from api.views.comment import CommentLISTView

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

router = routers.DefaultRouter()
router.register(r'news', news.NewsViewSet)
router.register(r'category', category.CategoryViewSet)
router.register(r'journey', journey.JourneyViewSet)
# router.register(r'comments', comment.CommentCommentsView, base_name='comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^user/', include('rest_auth.urls')),
    url(r'^user/registration/', include('rest_auth.registration.urls')),

    url(r'^comment/', CommentLISTView.as_view()),
]

urlpatterns += router.urls
