from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Restaurant, RestaurantPhoto, Review,
    Cuisine, CuisinePhoto, VisitorProfile, Visit
)
from .serializers import (
    RestaurantSerializer, RestaurantPhotoSerializer, ReviewSerializer,
    CuisineSerializer, CuisinePhotoSerializer, VisitorProfileSerializer, VisitSerializer
)

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100



class RestaurantListCreateView(ListCreateAPIView):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['city', 'cuisines__name']  
    search_fields = ['name', 'address']  
    ordering_fields = ['created_at', 'updated_at', 'average_rating'] 


class RestaurantDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RestaurantReviewsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            reviews = restaurant.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response({'detail': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)


class RestaurantPhotosView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            photos = restaurant.photos.all()
            serializer = RestaurantPhotoSerializer(photos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response({'detail': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

class RestaurantDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RestaurantReviewsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            reviews = restaurant.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response({'detail': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)


class RestaurantPhotosView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            photos = restaurant.photos.all()
            serializer = RestaurantPhotoSerializer(photos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response({'detail': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)


class CuisineListCreateView(ListCreateAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price', 'views']  
    search_fields = ['name']  
    ordering_fields = ['price', 'views']  


class CuisineDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CuisinePhotosView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            cuisine = Cuisine.objects.get(pk=pk)
            photos = cuisine.photos.all()
            serializer = CuisinePhotoSerializer(photos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cuisine.DoesNotExist:
            return Response({'detail': 'Cuisine not found'}, status=status.HTTP_404_NOT_FOUND)


class VisitorProfileListCreateView(ListCreateAPIView):
    queryset = VisitorProfile.objects.all()
    serializer_class = VisitorProfileSerializer
    permission_classes = [IsAuthenticated]


class VisitorProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = VisitorProfile.objects.all()
    serializer_class = VisitorProfileSerializer
    permission_classes = [IsAuthenticated]


class VisitListCreateView(ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['cuisine__name', 'visit_date']  
    search_fields = ['comment']  
    ordering_fields = ['expense', 'visit_date'] 

    def perform_create(self, serializer):
        visitor_profile = VisitorProfile.objects.get(user=self.request.user)
        serializer.save(visitor=visitor_profile)


class VisitDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['restaurant__name', 'rating']  
    search_fields = ['comment']  
    ordering_fields = ['created_at', 'rating']  

    def perform_create(self, serializer):
        visitor_profile = VisitorProfile.objects.get(user=self.request.user)
        serializer.save(visitor=visitor_profile)


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


































# @api_view(['GET', 'POST'])
# def cuisine_list_create(request):
#     if request.method == 'GET':
#         cuisines = Cuisine.objects.all()
#         serializer = CuisineSerializer(cuisines, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = CuisineSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def cuisine_detail_update_delete(request, pk):
#     try:
#         cuisine = Cuisine.objects.get(id=pk)
#     except Cuisine.DoesNotExist:
#         return Response({'detail': 'Cuisine not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CuisineSerializer(cuisine)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = CuisineSerializer(cuisine, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         cuisine.delete()
#         return Response({'detail': 'Cuisine deleted'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def visitor_profile(request):
#     profile = VisitorProfile.objects.get(user=request.user)
#     serializer = VisitorProfileSerializer(profile)
#     return Response(serializer.data)


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def visit_list_create(request):
#     if request.method == 'GET':
#         visits = Visit.objects.all()
#         serializer = VisitSerializer(visits, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = VisitSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def visitor_status(request):
#     profile = VisitorProfile.objects.get(user=request.user)
#     total_visits = Visit.total_visits(profile)
#     total_expenses = Visit.total_expenses(profile)
#     cuisines = Visit.cuisines_ordered(profile)

#     return Response({
#         'total_visits': total_visits,
#         'total_expenses': total_expenses,
#         'cuisines_ordered': cuisines
#     })
