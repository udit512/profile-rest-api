from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview =[
            'uses HTTP mathod as function(get,post,pathch,put,delete)'
            'Is similar to a trasitional Django View',
            'Gives you the most cntrol over your application login',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serealizer = self.serializer_class(data=request.data)

        if serealizer.is_valid():
            name = serealizer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serealizer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method','PATCH'})

    def delete(self,request,pk=None):
        """Delete an Object"""
        return Respons({'methon','DELETE'})
