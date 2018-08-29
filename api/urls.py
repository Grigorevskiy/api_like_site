from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from api.views.comment import CommentLISTView, JourneyCommentsDetailView
from api.views import news, category, journey, comment, faq, client_company, document


router = routers.DefaultRouter()
router.register(r'news', news.NewsViewSet)
router.register(r'category', category.CategoryViewSet)
router.register(r'journey', journey.JourneyViewSet)
router.register(r'faq', faq.FaqViewSet)
router.register(r'client_company', client_company.ClientCompanyViewSet)
router.register(r'documents', document.DocumentViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^journey/(?P<pk>[0-9]+)/comments/$', CommentLISTView.as_view()),
    url(r'^journey/(?P<pk>[0-9]+)/comments/(?P<com_pk>[0-9]+)/$', JourneyCommentsDetailView.as_view()),
    url(r'^user/', include('rest_auth.urls')),
    url(r'^user/registration/', include('rest_auth.registration.urls')),
]

urlpatterns += router.urls
