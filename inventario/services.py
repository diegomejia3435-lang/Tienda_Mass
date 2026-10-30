
from django.db.models import F
from catalogo.models import Producto


# Obtener productos que necesitan reposición
def obtener_productos_bajo_stock():

    productos = Producto.objects.filter(
        activo=True,
        stock__lte=F('stock_minimo')
    )

    return productos


# Regla para determinar si un producto necesita reposición
def necesita_reposicion(stock, stock_minimo):

    return stock <= stock_minimo
