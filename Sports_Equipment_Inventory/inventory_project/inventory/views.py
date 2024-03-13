# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Equipment
import json

@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data['name']
            quantity = data.get('quantity', 0)
            equipment = Equipment.objects.create(name=name, quantity=quantity)
            return JsonResponse({'id': equipment.id, 'name': equipment.name, 'quantity': equipment.quantity}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_item(request, equipment_id):
    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            equipment = Equipment.objects.get(pk=equipment_id)
            if 'quantity' in data:
                equipment.quantity = data['quantity']
                equipment.save()
            return JsonResponse({'id': equipment.id, 'name': equipment.name, 'quantity': equipment.quantity}, status=200)
        except Equipment.DoesNotExist:
            return JsonResponse({'error': 'Equipment not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_items(request):
    if request.method == 'GET':
        items = list(Equipment.objects.values())
        return JsonResponse(items, safe=False, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
