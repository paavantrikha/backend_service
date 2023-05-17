from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet

app_name = 'candidates'
router = DefaultRouter()

router.register('candidates_portal', CandidateViewSet)

urlpatterns = [
    *router.urls
]