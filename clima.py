import requests

API_KEY = "720678908a1bfc52b5aed3ef7ebc2d9d"  # Reemplazá con tu API Key real
CIUDAD = "Buenos Aires"  # Ciudad fija

def obtener_clima(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        temp = datos["main"]["temp"]
        descripcion = datos["weather"][0]["description"]
        print(f"\n🌤️ Clima en {ciudad}: {temp}°C, {descripcion.capitalize()}\n")
    else:
        print("⚠️ Error al obtener el clima. Verificá la API Key y el nombre de la ciudad.")

if __name__ == "__main__":
    obtener_clima(CIUDAD)
