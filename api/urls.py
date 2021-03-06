
from django.conf.urls import url
from rest_framework import routers
from api.views.comment import *
from api.views.news import *
from api.views.faq import *
from api.views.client_company import *
from api.views.document import *
from api.views.feedback import *
from api.views.journey import *
from api.views.accounts import *
from api.views.profile import *

from api.views.category import CategoryCreateListAPIView, CategoryDetailsAPIView
from api.views.order_anonymous import OrderAnonymousCreateAPIView, OrderAnonymousListAPIView, OrderAnonymousDetailsAPIView
from api.views.order import OrderAPIView, OrderDetailView


router = routers.DefaultRouter()
router.register(r'journey', JourneyViewSet)
router.register(r'news', NewsViewSet)
router.register(r'faq', FaqViewSet)
router.register(r'client_company', ClientCompanyViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'feedback', FeedBackViewSet)
router.register(r'journey/(?P<id>[0-9]+)/comments', JourneyCommentsViewSet, base_name='comments')


urlpatterns = [
    url(r'^user/(?P<user_id>[0-9]+)/profile/$', ProfileAPIView.as_view()),

    url(r'^user/login/$', LoginAPIView.as_view()),
    url(r'^user/logout/$', LogoutAPIView.as_view()),
    url(r'^user/registration/$', RegisterAPIView.as_view()),
    url(r'^user/change-password/$', ChangePasswordAPIView.as_view()),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),

    url(r'^journey/(?P<pk>[0-9]+)/order/$', OrderAPIView.as_view()),
    url(r'^journey/(?P<pk>[0-9]+)/order/(?P<order_pk>[0-9]+)/$', OrderDetailView.as_view()),

    url(r'^order_anonymous/$', OrderAnonymousListAPIView.as_view()),
    url(r'^order_anonymous/create/$', OrderAnonymousCreateAPIView.as_view()),
    url(r'^order_anonymous/(?P<pk>[0-9]+)/$', OrderAnonymousDetailsAPIView.as_view()),

    url(r'^category/$', CategoryCreateListAPIView.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryDetailsAPIView.as_view(), name='category-detail'),

    # url(r'^user/', include('rest_auth.urls')),
    # url(r'^user/registration/', include('rest_auth.registration.urls')),
]

urlpatterns += router.urls
