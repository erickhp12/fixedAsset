from django.shortcuts import render
from .serializers import MainSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Main


class SerializerMain(APIView):
    def get(self, request, format=None):
        snippets = Main.objects.all()
        serializer = MainSerializer(snippets, many=True)
        print "JSON RESPUESTA "
        print serializer.data
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Response": "Pedimento agregado correctamente"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_302_FOUND)


class SerializerSingleMain(APIView):
    def get(self, request, pk, format=None):
        snippets = Main.objects.get(id=pk)
        serializer = MainSerializer(snippets, many=False)
        print "JSON RESPUESTA "
        print serializer.data
        return Response(serializer.data)