from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import JobModel
from .models import JobApplicationModel
from .serializers import JobSerializer
from .serializers import JobApplicationSerializer

# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    model = JobModel
    queryset = model.objects.all()
    serializer_class = JobSerializer

    def list(self, request):
        try:
            print("Hi")
            job_queryset = self.model.objects.all()
            job_serializer = self.serializer_class(job_queryset, many=True)
            response = {
                "Success" : True,
                "Data" : job_serializer.data,
                "Message" : "Jobs Retrieved successfully"
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            response = {
                "Success" : False,
                "Error" : str(error),
                "Message" : "Internal Server Error"
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def create(self, request):
        try:
            data = request.data
            print(data)
            job_serializer = self.serializer_class(data=data)
            if job_serializer.is_valid():
                job_obj = job_serializer.save()
                response = {
                    "Success" : True,
                    "Data" : self.serializer_class(job_obj).data,
                    "Message" : "Job Posted Successfully"
                }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                response = {
                    "Success" : False,
                    "Error" : job_serializer.errors,
                    "Message" : "Enter correct and complete data to create User profile"
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            response = {
                "Success" : False,
                "Error" : str(error),
                "Message" : "Internal Server Error"
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class JobApplicationViewSet(viewsets.ModelViewSet):
    model = JobApplicationModel
    queryset = model.objects.all()
    serializer_class = JobApplicationSerializer

    def list(self, request):
        try:
            job_application_queryset = self.model.objects.all()
            job_application_serializer = self.serializer_class(job_application_queryset, many=True)
            response = {
                "Success" : True,
                "Data" : job_application_serializer.data,
                "Message" : "Jobs Applications Retrieved successfully"
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            response = {
                "Success" : False,
                "Error" : str(error),
                "Message" : "Internal Server Error"
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def create(self, request):
        try:
            data = request.data
            # print(data)
            job_application_serializer = self.serializer_class(data=data)
            if job_application_serializer.is_valid():
                job_obj = job_serializer.save()
                response = {
                    "Success" : True,
                    "Data" : self.serializer_class(job_obj).data,
                    "Message" : "Job Posted Successfully"
                }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                response = {
                    "Success" : False,
                    "Error" : job_serializer.errors,
                    "Message" : "Enter correct and complete data to create User profile"
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            response = {
                "Success" : False,
                "Error" : str(error),
                "Message" : "Internal Server Error"
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)