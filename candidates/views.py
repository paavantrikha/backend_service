from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CandidateModel
from .serializers import CandidateSerializer

# Create your views here.

class CandidateViewSet(viewsets.ModelViewSet):
    model = CandidateModel
    queryset = model.objects.all()
    serializer_class = CandidateSerializer

    def list(self, request):
        try:
            candidate_queryset = self.model.objects.all()
            candidate_serializer = self.serializer_class(candidate_queryset, many=True)
            response = {
                'success' : True,
                'data' : candidate_serializer.data,
                'message' : 'Candidates Data returned successfully.'
            }
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as error:
            response = {
                'success' : False,
                'error' : str(error),
                'message' : 'Internal server error'
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def create(self, request):
        try:
            data = request.data
            print(data)
            candidate_serializer = self.serializer_class(data=data)
            if candidate_serializer.is_valid():
                candidate_obj = candidate_serializer.save()
                response = {
                    'success' : True,
                    'data' : self.serializer_class(candidate_obj).data,
                    'message' : 'Candidate profile created successfully'
                }
                return Response(response, status=status.HTTP_201_CREATED)
            
            else:
                response = {
                    'success' : False,
                    'error' : candidate_serializer.errors,
                    'message' : 'Enter correct and complete data to create Candidate profile'
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as error:
            response ={
                'success' : False,
                'error' : str(error),
                'message' : 'Internal server error'
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


