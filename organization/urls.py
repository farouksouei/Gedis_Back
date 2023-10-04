from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'details', views.OrganizationDetailViewSet)

urlpatterns = router.urls
