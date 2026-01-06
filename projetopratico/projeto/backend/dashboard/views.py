from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import ChatbotRequest
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class DashboardView(APIView):
    permission_classes = [IsAuthenticated] #serve para proteger com jwt assim somente quem ta registrado tem acesso
    def get (self, request):
        now = timezone.now()

        data={
            "24h": ChatbotRequest.objects.filter(created_at__gte=now - timedelta(hours=24)).count(),
            "7d": ChatbotRequest.objects.filter(created_at__gte=now - timedelta(days=7)).count(),
            "30d": ChatbotRequest.objects.filter(created_at__gte =now - timedelta(days=30)).count(),
        }
        return Response(data)
    
class RegisterRequestView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        ChatbotRequest.objects.create()
        return Response(
            {"message": "Requisição registrada com sucesso"},
            status=status.HTTP_201_CREATED
        )