from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField

from core.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade", "total", "total2")
        depth = 2


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email")
    status = CharField(source="get_status_display")
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
