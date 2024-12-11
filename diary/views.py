from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Cuisine, CuisinePhoto, VisitorProfile, Visit
from .serializers import CuisineSerializer, CuisinePhotoSerializer, VisitorProfileSerializer, VisitSerializer


@api_view(['GET', 'POST'])
def cuisine_list_create(request):
    if request.method == 'GET':
        cuisines = Cuisine.objects.all()
        serializer = CuisineSerializer(cuisines, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CuisineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cuisine_detail_update_delete(request, pk):
    try:
        cuisine = Cuisine.objects.get(id=pk)
    except Cuisine.DoesNotExist:
        return Response({'detail': 'Cuisine not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CuisineSerializer(cuisine)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CuisineSerializer(cuisine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        cuisine.delete()
        return Response({'detail': 'Cuisine deleted'}, status=status.HTTP_204_NO_CONTENT)


# VisitorProfile Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def visitor_profile(request):
    profile = VisitorProfile.objects.get(user=request.user)
    serializer = VisitorProfileSerializer(profile)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def visit_list_create(request):
    if request.method == 'GET':
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def visitor_status(request):
    profile = VisitorProfile.objects.get(user=request.user)
    total_visits = Visit.total_visits(profile)
    total_expenses = Visit.total_expenses(profile)
    cuisines = Visit.cuisines_ordered(profile)

    return Response({
        'total_visits': total_visits,
        'total_expenses': total_expenses,
        'cuisines_ordered': cuisines
    })
