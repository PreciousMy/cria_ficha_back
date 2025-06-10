from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Usuario(models.Model):
    id = models.TextField()
    nome = models.TextField()
    senha = models.TextField()
    email = models.TextField()
    foto_perfil = models.CharField()

    def__str__(self): # type: ignore
        return f"{self.nome}" # type: ignore


class Ficha(models.Model):
    id = models.TextField()
    id_usuario = models.TextField()
    nome_Personagem =  models.TextField()
    nivel = models.IntegerField()
    classe =  models.TextField()
    raca = models.TextField()
    antecendente = models.TextField()
    alinhamento = models.TextField()
    experiencia = models.IntegerField()
    forca = models.IntegerField()
    mod_forca = models.IntegerField()
    destreza = models.IntegerField()
    mod_destreza = models.IntegerField()
    constituicao = models.IntegerField()
    mod_constituicao = models.IntegerField()
    inteligencia = models.IntegerField()
    mod_inteligencia = models.IntegerField()
    sabedoria = models.IntegerField()
    mod_sabedoria = models.IntegerField()
    carisma = models.IntegerField()
    mod_carisma = models.IntegerField()
    inspiracao = models.IntegerField()
    bonus_proeficiencia = models.IntegerField()
    idioma_proeficiencia= models.TextField()
    iniciativa = models.IntegerField()
    deslocamento = models.FloatField()
    pontos_vida = models.IntegerField()
    caracteristica_habilidade = models.TextField()
    dado_vida = models.TextField()
    ideias = models.TextField()
    taco_personalidade = models.TextField()
    vinculo = models.TextField()
    fraquesa = models.TextField()
    pv_totais = models.IntegerField()
    pPrata = models.IntegerField()
    pOuro = models.IntegerField()
    pEletro = models.IntegerField()
    pCobre = models.IntegerField()
    pLatina = models.IntegerField()
    descricao_Mag_Atk = models.TextField()
    equipamento_descricao = models.TextField()
    olho = models.TextField()
    idade = models.IntegerField()
    peso = models.FloatField()
    cabelo = models.TextField()
    altura = models.FloatField()
    pele = models.TextField()
    aparencia = models.TextField()
    historia_Personagem = models.TextField()
    tesoro = models.TextField()
    aliados_Org = models.TextField()

    def__str__(self): # type: ignore
        return f"{self.nome}" # type: ignore

class Pericia_Teste(models.Model):
    id_Pericia = models.TextField()
    id_Ficha = models.TextField()
    nome = models.TextField()
    valor = models.IntegerField()

    def__str__(self): # type: ignore
        return f"{self.nome}" # type: ignore

class Arma_Ataque(models.Model):
    nome_AM = models.TextField()
    id_Ficha = models.TextField()
    bonus_AM = models.IntegerField()

    def__str__(self): # type: ignore
        return f"{self.nome}" # type: ignore

class Arma (models.Model):
    id_Arma = models.TextField()
    id_AM  = models.TextField()
    nome = models.TextField()
    dano = models.TextField()
    tipo_dano = models.TextField()

    def__str__(self): # type: ignore
        return f"{self.nome}" # type: ignore

class Magia(models.Model):
    id_Magia = models.TextField()
    nome = models.TextField()
    nivel_magia = models.TextField()
    alcance = models.TextField()
    duracao = models.TextField()
    componentes = models.TextField()
    descricao = models.TextField()
    tempo_Conjuracao = models.TextField()

    def__str__(self): # type: ignore
        return f"{self.nome}" # type: ignore

class Lista_Magia(models.Model):
    id_Ficha = models.TextField()
    id_Magia = models.TextField()
    classe_conjurador = models.TextField()
    bonus_ataque = models.IntegerField()
    equipado_Em = models.TextField()
    CD_TR = models.IntegerField()
    habilidade_chave = models.TextField()

    def__str__(self): # type: ignore
        return f"{self.nome}" # type: ignore

class Armadura(models.Model):
    id_Armadura = models.TextField()
    nome =  models.TextField()
    tipo =  models.TextField()
    class_Armadura =  models.TextField() 

    def__str__(self): # type: ignore
        return f"{self.nome}" # type: ignore

class Classe_Armadura(models.Model):
    id_Ficha =  models.TextField()
    id_Armadura =  models.TextField()
    classe_modificador =  models.TextField()
    
    def__str__(self): # type: ignore
        return f"{self.nome}" # type: ignore
