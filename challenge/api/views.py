from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Sum
from api.models import Zone
# Create your views here.
@csrf_exempt
def sum_build(request):
    bat_id = request.GET.get("bat_id", 0)
    result = Zone.objects.filter(bat_id=bat_id).aggregate(total=Sum('surface'))
    if "total" in result:
        data = result["total"]
    else:
        data = None
    return JsonResponse({"result": data})