from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@api_view()
@permission_classes([IsAuthenticated])
def hello_world(request):
    return Response({"message": "Hello, world!"})


@login_required
# @permission_classes([IsAuthenticated])
def test(request):
    context = {
        'ay_7aga': vars(request)
    }
    return render(request, 'test1.html', context)
