from rest_framework import serializers
from .models import JobModel
from .models import JobApplicationModel

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = "__all__"

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationModel
        fields = "__all__"
