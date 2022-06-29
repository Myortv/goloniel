from django.urls import path

from rest_framework.routers import SimpleRouter

from account.views import MeUserApiView, SuperUserApiView, StrangerUserApiView


router = SimpleRouter()
router.register('api/admin', SuperUserApiView)

urlpatterns = [
    path('api/me', MeUserApiView.as_view(), name='my_account'),
    path('api/<int:pk>', StrangerUserApiView.as_view(), name='stranger_account'),
]

urlpatterns += router.urls
