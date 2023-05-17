from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate
import pyotp
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend
from .models import UserModel
from .serializers import UserSerializer, UserListSerializer
from rest_framework.decorators import api_view

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    model = UserModel
    queryset = model.objects.all()
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer

    def list(self, request):
        try:
            print('Hello')
            print('dddddddddddddddddddd')
            user_queryset = self.model.objects.all()
            user_serializer = self.list_serializer_class(user_queryset, many=True)
            response = {
                "Success" : True,
                "Data" : user_serializer.data,
                "Message" : "Users data returned successfuly"
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            response = {
                "Success" : False,
                "Error" : str(error),
                "Message" : "Internal server error"
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def create(self, request):
        try:
            data = request.data
            # print(data) # Shows in Visual Studio
            user_serializer = self.serializer_class(data=data)
            if user_serializer.is_valid():
                user_obj = user_serializer.save()
                response = {
                    "Success" : True,
                    "Data" : self.serializer_class(user_obj).data,
                    "Message" : "User created successfully"
                }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                response = {
                    "Success" : False,
                    "Error" : user_serializer.errors,
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
        
    
    @action(detail=False, methods=['post'], name="login") # For creating API.
    # @action is used to define custom actions in viewsets.
    # detail=False is to perform custom actions on the entire model, not just one instance. detail=True for single instance.
    def login(self, request): # Name of method is added to URL. For eg - url/login/
        try:
            data = request.data
            user_name = data["username"]   
            pwd = data["password"]         
            user_obj = UserModel.objects.filter(username=user_name) # Writing SQL query in python
            if not user_obj:
                response = {
                "Success" : False,
                "Message" : "User not found"
                }
                return Response(response, status=status.HTTP_404_NOT_FOUND)
            
            # user = authenticate(username=user_name, password=pwd)
            # print(user)
            # if user is None:
            #     response = {
            #         "Success" : False,
            #         "Message" : "Incorrect credentials entered"
            #     }
            #     return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            
            totp = pyotp.TOTP(pyotp.random_base32()) # TOTP: Time Based One Time Password. 
            # Valid for a short period of time, typically 30 seconds.
            otp = totp.now() #The now() method generates an OTP based on the current time and the secret key.    
            '''
            *OTP is sent to the user's email address using the send_mail function.
            *Parameters for send_mail function : subject, message, from_email, recipient_list, fail_silently=False.
            *fail_silently controls how the send_mail function behaves if it encounters an error while trying to send an email.
            *If fail_silently=True, the function will fail silently and return None if it encounters an error.
            *If fail_silently=False (the default), the function will raise an exception if it encounters an error.
            '''

            send_mail('Your OTP for logging in', f'Your OTP is: {otp}', 'dagaddalla1@gmail.com', #Sender email is configured in project's settings.py
                      [user_name.email], fail_silently=False)
            
            response = {
                    "Success" : True,
                    "Message" : "User logged in successfully"
                }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as error:
            response = {
                "Success" : False,
                "Error" : str(error),
                "Message" : "Internal Server Error"
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['post'])
    def mail(self, request):
        data = request.data
        print(data)
        mail = data.get('email')
        print(mail)
        totp = pyotp.TOTP(pyotp.random_base32())
        otp = totp.now()
        try:
            send_mail('Your OTP for logging in', f'Your OTP is: {otp}', 'dagaddalla@yahoo.com', [mail], fail_silently=False)

            response = {
                        "Success" : True,
                        "Message" : "Email sent successfully"
                    }
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as error:
            response = {
                        "Success" : False,
                        "Error" : str(error),
                        "Message" : "Can't send mail."
                    }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            


    

