from django.shortcuts import render
from rest_framework import filters, viewsets
from .models import Usuario, Ficha, Pericia_Teste, Arma_Ataque, Arma, Magia, Lista_Magia, Armadura, Classe_Armadura
from .serializers import UsuarioSerializer,Ficha, Pericia_TesteSerializer, Arma_AtaqueSerializer, ArmaSerializer,MagiaSerializer, Lista_MagiaSerializer, ArmaduraSerializer, Classe_ArmaduraSerializer

# Create your views here.
