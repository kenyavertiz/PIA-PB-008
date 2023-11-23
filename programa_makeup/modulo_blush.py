# 1. MODULO: BLUSH

import requests

#1. CATEGORY-CREAM 

def obtener_blushes_cream():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush&category=cream"

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
    obtener_blushes_cream()
    
#1. CATEGORY-POWDER

def obtener_blushes_powder():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush&category=powder"

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
    obtener_blushes_powder()

#2. MEJORES CALIFICADOS

def obtener_blushes_con_calificacion_superior(puntuacion):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush&rating_greater_than={puntuacion}"

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
    obtener_blushes_con_calificacion_superior(puntuacion_filtropuntuacion)

#3. PRECIO - MAS CARO

def obtener_blushes_con_precio_superior(valor):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush&price_greater_than={valor}"

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
    obtener_blushes_con_precio_superior(valor_filtroprecio)

#3. PRECIO - MAS BARATO 

def obtener_blushes_con_precio_menor(valor):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush&price_less_than={valor}"

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
    obtener_blushes_con_precio_menor(valor_filtroprecio)

#4. MARCAS

def obtener_blushes_por_marca():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()
            blushes_por_marca = {}

            for producto in datos:
                nombre = producto.get('name', 'Nombre no disponible')
                marca = producto.get('brand', 'Marca no disponible')

                if marca in blushes_por_marca:
                    blushes_por_marca[marca].append(nombre)
                else:
                    blushes_por_marca[marca] = [nombre]

            for marca, blushes in blushes_por_marca.items():
                print(f"Marca: {marca}")
                for blush in blushes:
                    print(f"  Nombre: {blush}")
                print()

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_blushes_por_marca()


#5. TONOS

def obtener_tonos_por_blush():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()
            tonos_por_blush = {}
            
            for producto in datos:
                nombre = producto.get('name', 'Nombre no disponible')
                tonos = producto.get('product_colors', [])
                tonos_por_blush[nombre] = tonos

            for nombre, tonos in tonos_por_blush.items():
                print(f"Blush: {nombre}")
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
    obtener_tonos_por_blush()