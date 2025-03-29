from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def generate_tags(request):
    title = request.data.get('title', '')
    
    if not title:
        return Response({'tags': []})

    
    tags = title.lower().split()

    return Response({'tags': tags})
