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


class FichaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ficha
        fields = "__all__"
        read_only_fields = ("usuario",)


class UsuarioSerializer(serializers.ModelSerializer):
    fichas = FichaSerializer(source="ficha_set", many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = ["url", "id", "username", "email", "fichas"]


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
