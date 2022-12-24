from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .aitu_ready import vse



@api_view(['POST'])
@permission_classes((AllowAny,))
def overall_score(request):
    return Response({"Minted NFT": vse(request.data['address'])})
