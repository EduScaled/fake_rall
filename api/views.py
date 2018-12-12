from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import CreateEducationalOpportunitySerializer, EducationalOpportunitySerializer
from core.models import EducationalOpportunity


class EducationalOpportunityCreateApi(CreateAPIView):
    serializer_class = CreateEducationalOpportunitySerializer


class EducationalOpportunityViewSet(ReadOnlyModelViewSet):
    serializer_class = EducationalOpportunitySerializer
    queryset = EducationalOpportunity.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        activity = self.request.query_params.get('activity', None)
        if activity:
            qs = qs.filter(activity=activity)
        return qs
