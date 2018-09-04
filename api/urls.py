
from django.conf.urls import url, include
from rest_framework import routers
from api.views.comment import JourneyCommentsView, JourneyCommentsDetail
from api.views.order import OrderAPIView, OrderDetailView
from api.views import news, category, journey, faq, client_company, document, order_anonymous


router = routers.DefaultRouter()
router.register(r'news', news.NewsViewSet)
router.register(r'category', category.CategoryViewSet)
router.register(r'journey', journey.JourneyViewSet)
router.register(r'faq', faq.FaqViewSet)
router.register(r'client_company', client_company.ClientCompanyViewSet)
router.register(r'documents', document.DocumentViewSet)
router.register(r'order_anonymous', order_anonymous.OrderAnonymousViewSet)


urlpatterns = [
    url(r'^journey/(?P<pk>[0-9]+)/order/$', OrderAPIView.as_view()),
    url(r'^journey/(?P<pk>[0-9]+)/order/(?P<order_pk>[0-9]+)/$', OrderDetailView.as_view()),

    url(r'^journey/(?P<pk>[0-9]+)/comments/$', JourneyCommentsView.as_view()),
    url(r'^journey/(?P<pk>[0-9]+)/comments/(?P<com_pk>[0-9]+)/$', JourneyCommentsDetail.as_view()),

    url(r'^user/', include('rest_auth.urls')),
    url(r'^user/registration/', include('rest_auth.registration.urls')),
]

urlpatterns += router.urls
