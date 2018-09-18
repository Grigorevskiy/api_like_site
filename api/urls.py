
from django.conf.urls import url, include
from rest_framework import routers
from api.views.comment import JourneyCommentsView, JourneyCommentsDetail
from api.views.category import CategoryCreateListAPIView, CategoryDetailsAPIView
from api.views.order_anonymous import OrderAnonymousCreateAPIView, OrderAnonymousListAPIView, OrderAnonymousDetailsAPIView
from api.views.order import OrderAPIView, OrderDetailView
from api.views.journey import JourneyCreateListAPIView, JourneyDetailsAPIView
from api.views import news, faq, client_company, document, feedback


router = routers.DefaultRouter()
router.register(r'news', news.NewsViewSet)
router.register(r'faq', faq.FaqViewSet)
router.register(r'client_company', client_company.ClientCompanyViewSet)
router.register(r'documents', document.DocumentViewSet)
router.register(r'feedback', feedback.FeedBackViewSet)


urlpatterns = [
    url(r'^journey/(?P<pk>[0-9]+)/order/$', OrderAPIView.as_view()),
    url(r'^journey/(?P<pk>[0-9]+)/order/(?P<order_pk>[0-9]+)/$', OrderDetailView.as_view()),

    url(r'^journey/$', JourneyCreateListAPIView.as_view()),
    url(r'^journey/(?P<pk>[0-9]+)/$', JourneyDetailsAPIView.as_view(), name='journey-detail'),

    url(r'^order_anonymous/$', OrderAnonymousListAPIView.as_view()),
    url(r'^order_anonymous/create/$', OrderAnonymousCreateAPIView.as_view()),
    url(r'^order_anonymous/(?P<pk>[0-9]+)/$', OrderAnonymousDetailsAPIView.as_view()),

    url(r'^category/$', CategoryCreateListAPIView.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryDetailsAPIView.as_view(), name='category-detail'),

    url(r'^journey/(?P<pk>[0-9]+)/comments/$', JourneyCommentsView.as_view()),
    url(r'^journey/(?P<pk>[0-9]+)/comments/(?P<com_pk>[0-9]+)/$', JourneyCommentsDetail.as_view(),
        name='comments-detail'),

    url(r'^user/', include('rest_auth.urls')),
    url(r'^user/registration/', include('rest_auth.registration.urls')),
]

urlpatterns += router.urls
