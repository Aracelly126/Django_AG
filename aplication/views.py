import numpy as np
import tensorflow as tf
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
import os

# Cargar modelo
modelo_path = os.path.join(os.path.dirname(__file__), "../modelo_c2f.keras")
if os.path.exists(modelo_path):
    modelo = tf.keras.models.load_model(modelo_path)
else:
    modelo = None


def index(request):
    """Renderiza la página principal con el frontend"""
    return render(request, 'index.html')


@csrf_exempt
@require_http_methods(["POST"])
def predict(request):
    """API para predecir conversión de Celsius a Fahrenheit"""
    try:
        data = json.loads(request.body)
        # Admite {"c": 17} o {"centigrados": 17}
        c = data.get("c", data.get("centigrados", None))

        if c is None:
            return JsonResponse({"error": "Falta el campo 'c' (centígrados)."}, status=400)

        if modelo is None:
            return JsonResponse({"error": "Modelo no cargado"}, status=500)

        x = np.array([[float(c)]], dtype=np.float32)
        y = modelo.predict(x, verbose=0)

        return JsonResponse({
            "centigrados": float(c),
            "fahrenheit": float(y[0][0])
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
