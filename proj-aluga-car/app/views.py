from rest_framework import viewsets
from .models import Carro, Locacao
from .serializers import CarroSerializer, LocacaoSerializer

# ModelViewSet fornece automaticamente as ações:
# .list() [GET /api/carros/], .create() [POST /api/carros/],
# .retrieve() [GET /api/carros/1/], .update() [PUT /api/carros/1/],
# .destroy() [DELETE /api/carros/1/]
class CarroViewSet(viewsets.ModelViewSet):
    # queryset define a consulta base no banco de dados para buscar os registros
    queryset = Carro.objects.all()
    # serializer_class indica qual serializer vai processar os dados desta view
    serializer_class = CarroSerializer


class LocacaoViewSet(viewsets.ModelViewSet):
    # OTIMIZAÇÃO ORM:
    # select_related('carro') faz um JOIN no SQL para buscar os dados do carro junto com a locação.
    # Isso evita o problema de performance 'N+1 queries' quando o 'carro_detail' for montado no JSON.
    queryset = Locacao.objects.select_related('carro').all()
    serializer_class = LocacaoSerializer