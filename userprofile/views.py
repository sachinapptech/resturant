from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import NotYourProfile,ProfileNotFound
from .models import UserProfile
from .rendereds import ProfileJSONRendered
from .serializers import UserProfileSerializer,UpdateUserProfileSerializer


class GetProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRendered]

    def get(self,request):
        user = self.request.user 
        user_profile = UserProfile.objects.get(user = user)
        serializer = UserProfileSerializer(user_profile,context={"request":request})
        return Response(serializer.data,status=status.HTTP_200_OK)


class UpdateProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRendered]

    serializer_class = UpdateUserProfileSerializer

    def patch(self,request,username):
        try:
            UserProfile.objects.get(user__username=username)
        except UserProfile.DoesNotExist:
            raise ProfileNotFound
        
        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile
        
        data = request.data
        serializer = UpdateUserProfileSerializer(
            instance = request.user.profile,data = data,partial=True
        )
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    