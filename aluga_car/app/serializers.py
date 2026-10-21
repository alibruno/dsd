from rest_framework import serializers
from .models import Carro, Locacao

# ModelSerializer cria automaticamente os campos baseados no seu modelo
class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro  # Indica qual model este serializer vai mapear
        # Lista explicita dos campos que serão enviados/recebidos no JSON.
        # Incluir o 'id' é fundamental para que o cliente da API saiba a chave primária.
        fields = ['id', 'marca', 'modelo', 'ano', 'placa', 'status', 'valor_diaria']


class LocacaoSerializer(serializers.ModelSerializer):
    # CAMPO DE LEITURA CUSTOMIZADO:
    # 1. CarroSerializer(): Renderiza o JSON completo do carro em vez de apenas o ID.
    # 2. source='carro': Aponta para o atributo/campo 'carro' do model Locacao.
    # 3. read_only=True: Diz ao DRF que este campo é usado APENAS para GET (leitura),
    #    evitando erros ao tentar criar/atualizar uma locação.
    carro_detail = CarroSerializer(source='carro', read_only=True)

    class Meta:
        model = Locacao
        # 'carro' (campo padrão da FK) recebe apenas o ID no POST/PUT (Escrita).
        # 'carro_detail' exibe todos os dados do veículo no GET (Leitura).
        fields = ['id', 'carro', 'carro_detail', 'data_inicio', 'data_fim', 'valor_total']