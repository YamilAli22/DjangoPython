def importe_total_carrito(request):
    importe_total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carrito"].items():
            importe_total = importe_total + float(value["precio"])
    else:
        importe_total = "Inicia sesión para acceder a la tienda"
            
    return {"importe_total_carrito": importe_total}