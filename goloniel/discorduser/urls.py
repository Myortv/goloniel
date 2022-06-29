from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import MyDiscordApiView, SuperDiscordApiView

router = SimpleRouter()
router.register(r'api/admin', SuperDiscordApiView)

urlpatterns = [
    path('api/me', MyDiscordApiView.as_view(), name='my_discord'),
]

urlpatterns += router.urls
