producto = input("¿Nombre del producto? ")
precio = float(input("¿Precio unitario? $"))
cantidad = int(input("¿Cantidad? "))

subtotal = precio * cantidad

print("\n--- RESUMEN DE COMPRA ---")
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio:.2f}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal:.2f}")
