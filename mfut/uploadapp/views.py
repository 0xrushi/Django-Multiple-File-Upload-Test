from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from uploadapp.serializers import BlogSerializer


class BlogView(GenericAPIView):
    serializer_class = BlogSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request,*args,**kwargs):
        try:
            serializer = self.get_serializer(data=request.data, context={'request':request})

            if serializer.is_valid():
                serializer.save()
                data =serializer.data
                return Response(data,status=status.HTTP_201_CREATED)
            else:
                data = {'error':serializer.errors}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            data = {'error':str(e)}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)