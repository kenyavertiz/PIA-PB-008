#4. MODULO MASCARA

import requests

#1. ETIQUETA - VEGAN

def obtener_mascaras_vegan():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=mascara&tag=vegan"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()

            for mascara in datos:
                nombre = mascara.get('name', 'Nombre no disponible')
                precio = mascara.get('price', 'Precio no disponible')
                print(f"Nombre: {nombre}, Precio: {precio}")

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_mascaras_vegan()

#1. ETIQUETA - HYPOALLERGRNIC

def obtener_mascaras_hipoalergenicas():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=mascara&category=hypoallergenic"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()

            for mascara in datos:
                nombre = mascara.get('name', 'Nombre no disponible')
                precio = mascara.get('price', 'Precio no disponible')
                print(f"Nombre: {nombre}, Precio: {precio}")

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_mascaras_hipoalergenicas()

#1. ETIQUETA - ORGANIC

def obtener_mascaras_organicas():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=mascara&category=organic"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()

            for mascara in datos:
                nombre = mascara.get('name', 'Nombre no disponible')
                precio = mascara.get('price', 'Precio no disponible')
                print(f"Nombre: {nombre}, Precio: {precio}")

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_mascaras_organicas()

#2. MEJOR CALIFICADOS

def obtener_mascaras_con_calificacion_superior(puntuacion):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_type=mascara&rating_greater_than={puntuacion}"

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
    obtener_mascaras_con_calificacion_superior(puntuacion_filtropuntuacion)


#3. PRECIO - MAS CARO

def obtener_mascaras_con_precio_superior(valor):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_type=mascara&price_greater_than={valor}"

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
    obtener_mascaras_con_precio_superior(valor_filtroprecio)

#3. PRECIO - MAS BARATO

def obtener_mascaras_con_precio_inferior(valor):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_type=mascara&price_less_than={valor}"

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
    obtener_mascaras_con_precio_inferior(valor_filtroprecio)

#4. MARCAS

def obtener_mascaras_por_marca():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=mascara"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()
            mascaras_por_marca = {}

            for producto in datos:
                nombre = producto.get('name', 'Nombre no disponible')
                marca = producto.get('brand', 'Marca no disponible')

                if marca in mascaras_por_marca:
                    mascaras_por_marca[marca].append(nombre)
                else:
                    mascaras_por_marca[marca] = [nombre]
                    
            for marca, mascaras in mascaras_por_marca.items():
                print(f"Marca: {marca}")
                for mascara in mascaras:
                    print(f"  Nombre: {mascara}")
                print()

        else:
            print(f"Error al obtener datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error de solicitud: {e}")

if __name__ == "__main__":
    obtener_mascaras_por_marca()

#5. TONOS

def obtener_tonos_por_mascara():
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type=mascara"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()
            tonos_por_mascara = {}

            for producto in datos:
                nombre = producto.get('name', 'Nombre no disponible')
                tonos = producto.get('product_colors', [])
                tonos_por_mascara[nombre] = tonos

            for nombre, tonos in tonos_por_mascara.items():
                print(f"Mascara: {nombre}")
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
    obtener_tonos_por_mascara()