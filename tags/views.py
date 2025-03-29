from django.http import JsonResponse
import json

def generate_tags(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        title = body.get('title', '')

        # TODO: Get tags
        tags = 0

        return JsonResponse({'tags': tags})
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)