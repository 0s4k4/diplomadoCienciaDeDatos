nombre = input('Introduce usuario: ')


if nombre == 'user':
    print('es usuario general el user')
elif nombre == 'admin':
    print('es admin el usuario')

elif nombre == 'externo':
    print('el usuario es externo')
else:
    print('no existe usuario en la base de datos')
