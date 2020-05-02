from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview =[
            'uses HTTP mathod as function(get,post,pathch,put,delete)'
            'Is similar to a trasitional Django View',
            'Gives you the most cntrol over your application login',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})
        
