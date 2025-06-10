from rest_framework import serializers

from .models import (
    Armaduras,
    Armas,
    Ataque,
    CaArmadura,
    Ficha,
    ListaMagia,
    Magias,
    Pericias,
    Usuario,
)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id_usuario", "nome", "email"]


class FichaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ficha
        fields = "__all__"


class PericiasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pericias
        fields = "__all__"


class ListaMagiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListaMagia
        fields = "__all__"


class MagiasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Magias
        fields = "__all__"


class ArmadurasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Armaduras
        fields = "__all__"


class CaArmadurasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaArmadura
        fields = "__all__"


class AtaqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ataque
        fields = "__all__"


class ArmasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Armas
        fields = "__all__"
