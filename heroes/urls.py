from rest_framework.routers import DefaultRouter

from .views import HeroApiViewSet

router = DefaultRouter()
router.register('', HeroApiViewSet)

urlpatterns = router.urls
