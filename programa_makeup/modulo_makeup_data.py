import requests
import json

#Se manda a llamar a la API y se piden los productos por categoria
def get_products_by_category(category):
  url = "http://makeup-api.herokuapp.com/api/v1/products.json"
  params = {"product_category": category}

  try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    products = response.json()
    return products
  except requests.RequestException as e:
    print(f"Error al obtener productos: {e}")
    return None

#Se hace la eliminacion de las imagenes inecesarias
def filtro_images(products):
  filtered_products = []
  for product in products:
    images = product.get('image_link', [])
    if not any(image.endswith('.jpg') for image in images):
      filtered_products.append(product)
  return filtered_products

#Se manda a llamar a la API y se piden los productos por etiqueta
def get_products_by_tag(tag):
  url = "http://makeup-api.herokuapp.com/api/v1/products.json"
  params = {"product_tags": tag}

  try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    products = response.json()
    return products
  except requests.RequestException as e:
    print(f"Error al obtener productos: {e}")
    return None

#Se guarda toda la informacion requerida en un archivo de texto
def save_to_file(filename, data):
  with open(filename, 'a', encoding='utf-8') as file:
    for item in data:
      file.write(json.dumps(item, ensure_ascii=False) + '\n')

# Función para guardar los datos consultados en un archivo de texto
def save_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(json.dumps(item, ensure_ascii=False) + '\n')
