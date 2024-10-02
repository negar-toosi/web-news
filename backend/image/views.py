from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ImageSerializer
from .models import Image

class ImageView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        image_serializer = ImageSerializer(
            data={
                "image" : request.FILES.get("media"),
            },
            context={"request": request}
        )

        if image_serializer.is_valid():
            image_serializer.save()
            return Response(
                {
                    "message": "image uploaded successfully",
                    "data": image_serializer.data,
                },
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": image_serializer.errors, "data" : None},
                status = status.HTTP_400_BAD_REQUEST,
            )
    def get(self, request):
        images = Image.objects.all()
        images_serializer = ImageSerializer(images, many=True)
        return Response(images_serializer.data,status = status.HTTP_200_OK)
                
