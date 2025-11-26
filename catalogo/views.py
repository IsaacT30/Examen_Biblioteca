from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from .models import Libro
from .serializers import LibroSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


@api_view(['POST'])
def prestamos_semana(request):
    data = request.data
    prestamos = data.get('prestamosPorDia')
    if not isinstance(prestamos, list) or len(prestamos) != 7:
        return Response({'detail': 'prestamosPorDia debe ser un arreglo de 7 números'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        total = sum(float(x) for x in prestamos)
    except (TypeError, ValueError):
        return Response({'detail': 'prestamosPorDia debe contener solo números'}, status=status.HTTP_400_BAD_REQUEST)

    promedio = total / 7

    if total < 10:
        mensaje = 'Poca actividad de préstamo'
    elif 10 <= total <= 30:
        mensaje = 'Actividad normal'
    else:
        mensaje = 'Alta demanda de libros'

    return Response({'totalPrestamos': total, 'promedioDiario': promedio, 'mensaje': mensaje})




