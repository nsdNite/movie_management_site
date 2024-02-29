from rest_framework.routers import DefaultRouter

from api_drf.views import ActorViewSet, DirectorViewSet, MovieViewSet

router = DefaultRouter()
router.register(r"actors", ActorViewSet)
router.register("directors", DirectorViewSet)
router.register("movies", MovieViewSet)

urlpatterns = router.urls

app_name = "api_drf"
