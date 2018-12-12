from rest_framework import serializers

from core.models import EducationalOpportunity


class EducationalOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalOpportunity
        fields = ('id', 'scales', 'activity')
        read_only_fields = ('id',)


class CreateEducationalOpportunitySerializer(serializers.Serializer):
    count = serializers.IntegerField(required=True, min_value=1, allow_null=False, write_only=True)
    activity = serializers.CharField(max_length=50, allow_null=False, allow_blank=False, write_only=True)

    def create(self, validated_data):
        count = validated_data['count']
        activity = validated_data['activity']

        educational_opportunities = []
        for _ in range(count):
            educational_opportunities.append(
                EducationalOpportunity.objects.create_random(activity=activity, submit=False))
        EducationalOpportunity.objects.bulk_create(educational_opportunities)
        return educational_opportunities
