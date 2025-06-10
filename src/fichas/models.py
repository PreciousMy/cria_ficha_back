from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=100, default="fulano")
    email = models.CharField(max_length=70, default="email@gmail.com")
    senha = models.CharField(blank=False, default="senhaFraca")

    fichas = models.ManyToManyField(
        "Ficha", related_name="lista", default=None, blank=True
    )

    def __str__(self):
        return f"{self.nome}"


class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)

    forc = models.IntegerField()
    dest = models.IntegerField()
    consti = models.IntegerField()
    inte = models.IntegerField()
    sab = models.IntegerField()
    car = models.IntegerField()
    forcMod = models.IntegerField()
    destMod = models.IntegerField()
    constiMod = models.IntegerField()
    inteMod = models.IntegerField()
    sabMod = models.IntegerField()
    carMod = models.IntegerField()
    bonusProef = models.IntegerField()
    inspira = models.IntegerField()
    sabPassiva = models.IntegerField()

    nomePerso = models.CharField(max_length=100)
    antecendente = models.CharField(max_length=70)
    exp = models.IntegerField()
    nivel = models.IntegerField()
    classe = models.CharField(max_length=70)
    alinhamento = models.CharField(max_length=70)
    raca = models.CharField(max_length=70)
    idiomas_Proeficiencias = models.TextField(
        max_length=500, blank=True, null=True, default=""
    )

    iniciativa = models.IntegerField()
    qtd_DadosVida = models.IntegerField()
    ideais = models.TextField(max_length=500, blank=True, null=True, default="")
    vinculos = models.TextField(max_length=500, blank=True, null=True, default="")
    tracosPerso = models.TextField(max_length=500, blank=True, null=True, default="")
    fraquezas = models.TextField(max_length=500, blank=True, null=True, default="")
    caractHabilidades = models.TextField(
        max_length=500, blank=True, null=True, default=""
    )
    pvTotais = models.IntegerField()
    dadoVida = models.CharField(max_length=7)
    deslocamento = models.FloatField()

    pCobre = models.IntegerField()
    pPrata = models.IntegerField()
    pOuro = models.IntegerField()
    pEletro = models.IntegerField()
    pPlatina = models.IntegerField()
    descAtaque = models.TextField(max_length=500, blank=True, null=True, default="")
    descEquip = models.TextField(max_length=500, blank=True, null=True, default="")

    olhos = models.CharField(max_length=50)
    cabelos = models.CharField(max_length=50)
    idade = models.IntegerField()
    altura = models.FloatField()
    peso = models.FloatField()
    pele = models.CharField(max_length=50)

    aparencia = models.TextField(max_length=500, blank=True, null=True, default="")
    aliadosOrg = models.TextField(max_length=500, blank=True, null=True, default="")
    outrasCaract = models.TextField(max_length=500, blank=True, null=True, default="")
    historia = models.TextField(max_length=500, blank=True, null=True, default="")
    tesouro = models.TextField(max_length=500, blank=True, null=True, default="")

    publica = models.BooleanField(default=False)

    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nomePerso}"


class ListaMagia(models.Model):

    habiChave = models.CharField(max_length=70)
    cdTR = models.IntegerField()
    bonusAtq = models.IntegerField()
    classeConju = models.CharField(max_length=100)
    slot = models.CharField(max_length=30)

    ficha = models.ForeignKey("Ficha", on_delete=models.CASCADE, null=True)
    magia = models.ForeignKey("Magias", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ficha}: {self.slot}- {self.magia}"


class Magias(models.Model):
    id_magias = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=100)
    alcance = models.FloatField()
    duracao = models.CharField(max_length=60)
    tempoConju = models.CharField(max_length=60)
    componentes = models.CharField(max_length=40)
    descricao = models.TextField(max_length=500, blank=True, null=True, default="")
    nivel = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nivel} - {self.nome}"


class Pericias(models.Model):
    id_pericias = models.AutoField(primary_key=True)

    valor = models.IntegerField(default=2)
    nome = models.CharField(max_length=40)

    ficha = models.ForeignKey("Ficha", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.ficha}: +{self.valor} {self.nome}"


class Ataque(models.Model):

    bonus = models.IntegerField()

    ficha = models.ForeignKey("Ficha", on_delete=models.CASCADE, null=True)
    arma = models.ForeignKey("Armas", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ficha}: {self.arma} +{self.bonus}"


class Armas(models.Model):
    id_armas = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=70)
    dano = models.CharField(max_length=7)
    tipoDano = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome} +{self.dano}"


class CaArmadura(models.Model):

    caMod = models.IntegerField()

    ficha = models.ForeignKey("Ficha", on_delete=models.CASCADE, null=True)
    armadura = models.ForeignKey("Armaduras", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ficha}: {self.armadura} = {self.caMod}"


class Armaduras(models.Model):
    id_armadura = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=70)
    ca = models.IntegerField()
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome} - {self.tipo}"