from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import EducationalOpportunityViewSet, EducationalOpportunityCreateApi

router = SimpleRouter()
router.register(r'educational_opportunities', EducationalOpportunityViewSet)

urlpatterns = [
    path('educational_opportunities/random/', EducationalOpportunityCreateApi.as_view(),
         name='create_random_educational_opportunities'),
    path('', include(router.urls)),
]
