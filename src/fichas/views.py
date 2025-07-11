from rest_framework import permissions, viewsets

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
from .serializers import (
    ArmadurasSerializer,
    ArmasSerializer,
    AtaqueSerializer,
    CaArmadurasSerializer,
    FichaSerializer,
    ListaMagiaSerializer,
    MagiasSerializer,
    PericiasSerializer,
    UsuarioSerializer,
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class FichaViewSet(viewsets.ModelViewSet):
    serializer_class = FichaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ficha.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class PericiasViewSet(viewsets.ModelViewSet):
    queryset = Pericias.objects.all()
    serializer_class = PericiasSerializer


class ListaMagiaViewSet(viewsets.ModelViewSet):
    queryset = ListaMagia.objects.all()
    serializer_class = ListaMagiaSerializer


class MagiasViewSet(viewsets.ModelViewSet):
    queryset = Magias.objects.all()
    serializer_class = MagiasSerializer


class ArmadurasViewSet(viewsets.ModelViewSet):
    queryset = Armaduras.objects.all()
    serializer_class = ArmadurasSerializer


class CaArmadurasViewSet(viewsets.ModelViewSet):
    queryset = CaArmadura.objects.all()
    serializer_class = CaArmadurasSerializer


class AtaqueViewSet(viewsets.ModelViewSet):
    queryset = Ataque.objects.all()
    serializer_class = AtaqueSerializer


class ArmasViewSet(viewsets.ModelViewSet):
    queryset = Armas.objects.all()
    serializer_class = ArmasSerializer


class FichaPublicaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FichaSerializer

    def get_queryset(self):
        return Ficha.objects.filter(publica=True)
