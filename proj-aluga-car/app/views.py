from rest_framework import viewsets
from .models import Carro, Locacao
from .serializers import CarroSerializer, LocacaoSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# ModelViewSet fornece automaticamente as ações:
# .list() [GET /api/carros/], .create() [POST /api/carros/],
# .retrieve() [GET /api/carros/1/], .update() [PUT /api/carros/1/],
# .destroy() [DELETE /api/carros/1/]
class CarroViewSet(viewsets.ModelViewSet):
    # queryset define a consulta base no banco de dados para buscar os registros
    queryset = Carro.objects.all()
    # serializer_class indica qual serializer vai processar os dados desta view
    serializer_class = CarroSerializer
    # Qualquer um pode ver os carros (GET), mas apenas usuários autenticados podem criar/editar/deletar
    permission_classes = [IsAuthenticatedOrReadOnly]


class LocacaoViewSet(viewsets.ModelViewSet):
    # OTIMIZAÇÃO ORM:
    # select_related('carro') faz um JOIN no SQL para buscar os dados do carro junto com a locação.
    # Isso evita o problema de performance 'N+1 queries' quando o 'carro_detail' for montado no JSON.
    queryset = Locacao.objects.select_related('carro').all()
    serializer_class = LocacaoSerializer
    # Exige que o usuário esteja autenticado via JWT para qualquer operação nesta view
    permission_classes = [IsAuthenticated]