precio_usd = '$242.00'
precio_usd = float(precio_usd[1:])
precio_euro = '189.87€'
precio_euro = float(precio_euro[:-1])
assert precio_euro < precio_usd , 'El valor del Precio en EURO es Mayor que el del Dolar'
