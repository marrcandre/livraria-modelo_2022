from rest_framework.viewsets import ModelViewSet

from core.serializers import UsuarioSerializer
from usuario.models import Usuario


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
