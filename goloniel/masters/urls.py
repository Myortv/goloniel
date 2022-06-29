from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
                MePlayerApi,
                SuperPlayerApi,
                MeMasterApi,
                SuperMasterApi,
            )

router = SimpleRouter()
router.register(r'api/player/admin', SuperPlayerApi)
router.register(r'api/master/admin', SuperMasterApi)

urlpatterns = [
    path('api/player', MePlayerApi.as_view(), name='me_player'),
    path('api/master', MeMasterApi.as_view(), name='me_master'),
]

urlpatterns += router.urls
