from django.shortcuts import render
from rest_framework import filters, viewsets
from .models import Usuario, Ficha, Pericia_Teste, Arma_Ataque, Arma, Magia, Lista_Magia, Armadura, Classe_Armadura
from .serializers import UsuarioSerializer,FichaSerializer, Pericia_TesteSerializer, Arma_AtaqueSerializer, ArmaSerializer,MagiaSerializer, Lista_MagiaSerializer, ArmaduraSerializer, Classe_ArmaduraSerializer

# Create your views here.

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FichaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer

class Pericia_TesteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pericia_Teste.objects.all()
    serializer_class = Pericia_TesteSerializer

class Arma_AtaqueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Arma_Ataque.objects.all()
    serializer_class = Arma_AtaqueSerializer

class ArmaiewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

class MagiaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Magia.objects.all()
    serializer_class = MagiaSerializer

class Lista_MagiaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lista_Magia.objects.all()
    serializer_class = Lista_MagiaSerializer

class ArmaduraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Armadura.objects.all()
    serializer_class = ArmaduraSerializer

class Classe_ArmaduraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Classe_Armadura.objects.all()
    serializer_class = Classe_ArmaduraSerializer