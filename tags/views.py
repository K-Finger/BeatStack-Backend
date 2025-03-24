from django.http import JsonResponse

def api_success(request):
    return JsonResponse({"message": "API successfully called"})