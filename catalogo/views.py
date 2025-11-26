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


@api_view(['POST'])
def prestamos_multa(request):
    data = request.data
    try:
        dias = int(data.get('diasRetraso', 0))
    except (TypeError, ValueError):
        return Response({'detail': 'diasRetraso debe ser un número entero'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        multa_por_dia = float(data.get('multaPorDia', 0))
    except (TypeError, ValueError):
        return Response({'detail': 'multaPorDia debe ser un número'}, status=status.HTTP_400_BAD_REQUEST)

    if dias <= 0:
        multa = 0
        mensaje = 'Sin retraso'
    else:
        multa = dias * multa_por_dia
        if multa <= 5:
            mensaje = 'Retraso leve'
        elif 5 < multa <= 15:
            mensaje = 'Retraso moderado'
        else:
            mensaje = 'Retraso grave, revisar con administración'

    return Response({'diasRetraso': dias, 'multa': multa, 'mensaje': mensaje})


