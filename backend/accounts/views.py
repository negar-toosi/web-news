from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializers import *
from rest_framework import permissions, status
from .validations import custom_validation
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser

class RegisterView(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
class AuthorRegisterView(APIView):
    # permission_classes = (permissions.AllowAny,)
    # parser_classes = (MultiPartParser, FormParser)
    # def post(self, request):
    #     data = request.data.copy()
    #     clean_data = custom_validation(data) 
    #     serializer = AuthorSerializer(data=clean_data) 
    #     if serializer.is_valid():
    #         Author = serializer.create(clean_data)
    #         Author.save() 
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    parser_classes = (MultiPartParser, JSONParser)
    serializer_class = AuthorSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )