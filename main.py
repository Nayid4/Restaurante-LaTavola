from flask import Flask, jsonify, redirect, request, render_template, url_for


app = Flask(__name__)

listProductos = [
    {"codigo": "001", "nombre": "Pizza Margarita", "descripcion": "Deliciosa pizza con salsa de tomate y queso mozzarella", "iva": "SI", "stock": 20, "precio": 10.99},
    {"codigo": "002", "nombre": "Espaguetis a la Carbonara", "descripcion": "Espaguetis con salsa de crema de leche, queso, huevo y panceta", "iva": "SI", "stock": 15, "precio": 12.50},
    {"codigo": "003", "nombre": "Lasagna Bolognesa", "descripcion": "Clásica lasaña de carne con salsa de tomate y queso parmesano", "iva": "SI", "stock": 12, "precio": 14.75},
    {"codigo": "004", "nombre": "Risotto de Champiñones", "descripcion": "Risotto cremoso con champiñones frescos y queso parmesano", "iva": "SI", "stock": 18, "precio": 11.99},
    {"codigo": "005", "nombre": "Tiramisú", "descripcion": "Postre italiano tradicional hecho con café, bizcochos, mascarpone y cacao en polvo", "iva": "SI", "stock": 25, "precio": 7.99},
    {"codigo": "006", "nombre": "Cannoli Siciliani", "descripcion": "Dulce italiano típico de Sicilia hecho con masa frita y relleno de ricota y chocolate", "iva": "SI", "stock": 30, "precio": 3.50},
    {"codigo": "007", "nombre": "Gelato de Limón", "descripcion": "Helado italiano de limón refrescante y cremoso", "iva": "SI", "stock": 22, "precio": 4.99},
    {"codigo": "008", "nombre": "Panini Caprese", "descripcion": "Panini relleno con mozzarella, tomate, albahaca y aceite de oliva", "iva": "SI", "stock": 17, "precio": 8.25}
]

@app.route('/')
def principal():
    print(url_for('principal'))
    
    return render_template('principal.html')

@app.route('/nosotros')
def nosotros():
    return render_template('Nosotros.html')

@app.route('/clientes')
def clientes():
    clientes = [
        {"nombre": "Juan", "apellido": "Pérez", "cedula": "123456789", "correo": "juan@example.com", "ciudad": "Ciudad de México", "discapacidad": "NO"},
        {"nombre": "María", "apellido": "García", "cedula": "987654321", "correo": "maria@example.com", "ciudad": "Bogotá", "discapacidad": "SI"},
        {"nombre": "Carlos", "apellido": "López", "cedula": "456789123", "correo": "carlos@example.com", "ciudad": "Madrid", "discapacidad": "NO"},
        {"nombre": "Laura", "apellido": "Martínez", "cedula": "789123456", "correo": "laura@example.com", "ciudad": "Santiago", "discapacidad": "SI"},
        {"nombre": "Pedro", "apellido": "Sánchez", "cedula": "321654987", "correo": "pedro@example.com", "ciudad": "Buenos Aires", "discapacidad": "NO"},
        {"nombre": "Ana", "apellido": "Rodríguez", "cedula": "654987321", "correo": "ana@example.com", "ciudad": "Lima", "discapacidad": "NO"},
        {"nombre": "Daniel", "apellido": "Hernández", "cedula": "987321654", "correo": "daniel@example.com", "ciudad": "São Paulo", "discapacidad": "SI"},
        {"nombre": "Sofía", "apellido": "Díaz", "cedula": "159487263", "correo": "sofia@example.com", "ciudad": "Montevideo", "discapacidad": "NO"},
        {"nombre": "Diego", "apellido": "Gómez", "cedula": "369258147", "correo": "diego@example.com", "ciudad": "Lisboa", "discapacidad": "SI"},
        {"nombre": "Paula", "apellido": "Fernández", "cedula": "852369741", "correo": "paula@example.com", "ciudad": "Quito", "discapacidad": "NO"}
    ]

    return render_template('ListadoDeClientes.html', clientes=clientes)

@app.route('/agregar-producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        # Obtener los datos del formulario
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        stock = request.form['stock']
        precio = request.form['precio']
        iva = request.form['iva']
        
        # Validar el campo de código (debe ser numérico)
        if not codigo.isdigit():
            return "El código debe ser un valor numérico.", 400
        
        # Validar el campo de precio (debe ser un número positivo)
        try:
            precio = float(precio)
            if precio <= 0:
                raise ValueError("El precio debe ser un número positivo.")
        except ValueError as e:
            return str(e), 400

        # Crear un nuevo producto
        nuevo_producto = {
            'codigo': codigo,
            'nombre': nombre,
            'descripcion': descripcion,
            'stock': stock,
            'precio': precio,
            'iva': iva
        }
        
        # Agregar el nuevo producto a la lista de productos
        listProductos.append(nuevo_producto)
        
        # Redireccionar a la página de productos después de agregar el producto
        return redirect(url_for('productos'))
    
    # Si es una solicitud GET, simplemente renderiza el formulario
    return render_template('AgregarProductos.html')

@app.route('/productos')
def productos():
    return render_template('ListadoDeProductos.html', productos=listProductos)


@app.route('/promociones')
def promociones():
    promociones = [
        {"nombre": "Promoción 1", "imagen": "promo1.jpg"},
        {"nombre": "Promoción 2", "imagen": "promo2.jpg"},
        {"nombre": "Promoción 3", "imagen": "promo3.jpg"},
        {"nombre": "Promoción 4", "imagen": "promo4.jpg"},
        {"nombre": "Promoción 5", "imagen": "promo5.jpg"},
        {"nombre": "Promoción 6", "imagen": "promo6.jpg"},
        {"nombre": "Promoción 7", "imagen": "promo7.jpg"},
        {"nombre": "Promoción 8", "imagen": "promo8.jpg"},
        # Agrega más promociones según sea necesario
    ]

    return render_template('Promociones.html', promociones=promociones)


if __name__ in "__main__":
    app.run(debug=True)