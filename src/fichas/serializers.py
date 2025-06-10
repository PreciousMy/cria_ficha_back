from rest_framework import serializers
from .models import Usuario, Ficha, Pericia_Teste, Arma_Ataque, Arma, Magia, Lista_Magia, Armadura, Classe_Armadura

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("nome", "email"," foto_perfil" )  # Eu acho que deve olcutar a senha

class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = '__all__'

class Pericia_TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pericia_Teste
        fields = '__all__'

class Arma_AtaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma_Ataque
        fields = '__all__'

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = '__all__'

class MagiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magia
        fields = '__all__'

class Lista_MagiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista_Magia
        fields = '__all__'

class ArmaduraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armadura
        fields = '__all__'

class Classe_ArmaduraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe_Armadura
        fields = '__all__'