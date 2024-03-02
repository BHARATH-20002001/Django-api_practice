from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from api.models import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from api.serializers import *

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def SchoolJsonData(request):
    SOD = School.objects.all()
    JOD = SchoolModelSerializer(SOD,many=True)
    jsondata = JOD.data
    return Response(jsondata)