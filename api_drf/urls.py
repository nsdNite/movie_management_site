from rest_framework.routers import DefaultRouter

from api_drf.views import ActorViewSet

router = DefaultRouter()
router.register(r"actors", ActorViewSet)

urlpatterns = router.urls

app_name = "api_drf"
