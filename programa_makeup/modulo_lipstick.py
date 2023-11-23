#3. MODULO LIPSTICK

import requests

#1. CATEGORIA - LIPSTICK

def obtener_lipsticks_en_categoria_lipstick():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=lipstick&category=lipstick"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()

            for lipstick in datos:
                nombre = lipstick.get('name', 'Nombre no disponible')
                precio = lipstick.get('price', 'Precio no disponible')
                print(f"Nombre: {nombre}, Precio: {precio}")

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_lipsticks_en_categoria_lipstick()

#1. CATEGORIA - LIP_GLOSS

def obtener_lipsticks_en_categoria_lip_gloss():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=lipstick&category=lip_gloss"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()

            for lipstick in datos:
                nombre = lipstick.get('name', 'Nombre no disponible')
                precio = lipstick.get('price', 'Precio no disponible')
                print(f"Nombre: {nombre}, Precio: {precio}")

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_lipsticks_en_categoria_lip_gloss()

#1. CATEGORIA - LIQUID

def obtener_lipsticks_en_categoria_liquid():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=lipstick&category=liquid"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()

            for lipstick in datos:
                nombre = lipstick.get('name', 'Nombre no disponible')
                precio = lipstick.get('price', 'Precio no disponible')
                print(f"Nombre: {nombre}, Precio: {precio}")

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_lipsticks_en_categoria_liquid()

#1. CATEGORIA - LIP_STAIN

def obtener_lipsticks_en_categoria_lip_stain():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=lipstick&category=lip_stain"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()

            for lipstick in datos:
                nombre = lipstick.get('name', 'Nombre no disponible')
                precio = lipstick.get('price', 'Precio no disponible')
                print(f"Nombre: {nombre}, Precio: {precio}")

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_lipsticks_en_categoria_lip_stain()

#2. MEJOR CALIFICADOS

def obtener_lipsticks_con_calificacion_superior(puntuacion):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_type=lipstick&rating_greater_than={puntuacion}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()
            suma_calificaciones = 0

            for producto in datos:
                nombre = producto.get('name', 'Nombre no disponible')
                calificacion = producto.get('rating', 'Calificación no disponible')
                suma_calificaciones += float(calificacion)
                print(f"Nombre: {nombre}, Calificación: {calificacion}")
            print(" ")    
            print("La operacion matematica es: ")
            print(f"La suma total de calificaciones de los {len(datos)} productos es de: {suma_calificaciones}")

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    puntuacion_filtropuntuacion = 4.0
    obtener_lipsticks_con_calificacion_superior(puntuacion_filtropuntuacion)


#3. PRECIO - MAS CARO

def obtener_lipsticks_con_precio_superior(valor):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_type=lipstick&price_greater_than={valor}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()

            for producto in datos:
                nombre = producto.get('name', 'Nombre no disponible')
                precio = producto.get('price', 'Precio no disponible')
                print(f"Nombre: {nombre}, Precio: {precio}")

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    valor_filtroprecio = 10
    obtener_lipsticks_con_precio_superior(valor_filtroprecio)

#3.PRECIO - MAS BARATO

def obtener_lipsticks_con_precio_inferior(valor):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_type=lipstick&price_less_than={valor}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()

            for producto in datos:
                nombre = producto.get('name', 'Nombre no disponible')
                precio = producto.get('price', 'Precio no disponible')
                print(f"Nombre: {nombre}, Precio: {precio}")

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    valor_filtroprecio = 10
    obtener_lipsticks_con_precio_inferior(valor_filtroprecio)

#4. MARCAS

def obtener_lipsticks_por_marca():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=lipstick"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()
            lipsticks_por_marca = {}

            for producto in datos:
                nombre = producto.get('name', 'Nombre no disponible')
                marca = producto.get('brand', 'Marca no disponible')

                if marca in lipsticks_por_marca:
                    lipsticks_por_marca[marca].append(nombre)
                else:
                    lipsticks_por_marca[marca] = [nombre]

            for marca, lipsticks in lipsticks_por_marca.items():
                print(f"Marca: {marca}")
                for lipstick in lipsticks:
                    print(f"  Nombre: {lipstick}")
                print()

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_lipsticks_por_marca()

#5. TONOS

def obtener_tonos_por_lipstick():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=lipstick"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()
            tonos_por_lipstick = {}

            for producto in datos:
                nombre = producto.get('name', 'Nombre no disponible')
                tonos = producto.get('product_colors', [])

                tonos_por_lipstick[nombre] = tonos

            for nombre, tonos in tonos_por_lipstick.items():
                print(f"Lipstick: {nombre}")
                if tonos:
                    for tono in tonos:
                        nombre_tono = tono.get('colour_name', 'Nombre no disponible')
                        print(f"  Tono: {nombre_tono}")
                else:
                    print("  No hay información de tonos disponible.")
                print()

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_tonos_por_lipstick()