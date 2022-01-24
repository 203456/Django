from rest_framework import routers, serializers, viewsets
# Importación de modelos
from primerComponente.models import primerTabla
class primerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = primerTabla
        fields = ['nombre', 'edad']