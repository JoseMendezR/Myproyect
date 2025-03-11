refraccion = 100000
seguir = True
while seguir:
    cantidad = input("Ingrese el número de refracciones a comprar ($100000 x Unidad):")

    if cantidad.isdigit():
        cantidad = int(cantidad)
        total = cantidad * refraccion

        if total > 500000:
            inversion = (total * 55) / 100
            prestamo = (total * 30) / 100
            credito = (total * 15) / 100
            total_final = total + (credito * 20) / 100
            print("=" * 80)
            print(f"""-Piezas compradas: {cantidad}
        -Precio Unitario: ${refraccion}
        -Inversión de la empresa (55%): ${inversion}
        -Préstamo al banco (30%): ${prestamo}
        -Crédito al fabricante (15%): ${credito}
        ===================================================================================
        -Monto total de la compra: {total_final}
        """)

        elif total < 500000:
            inversion = (total * 70) / 100
            credito = (total * 30) / 100
            total_final = total + (credito * 20) / 100
            print("=" * 80)
            print(f"""-Piezas compradas: {cantidad}
        -Precio Unitario: ${refraccion}
        -Inversión de la empresa (70%): ${inversion}
        -Préstamo al banco (0%): $0
        -Crédito al fabricante (30%): ${credito}
        ===================================================================================
        -Monto total de la compra: {total_final}
        """)
        seguir = False 
    else:
        print("No se ha ingresado un número válido. Intente de nuevo.")