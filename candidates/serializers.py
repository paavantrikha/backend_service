from rest_framework import serializers
from .models import CandidateModel

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateModel
        fields = "__all__"
