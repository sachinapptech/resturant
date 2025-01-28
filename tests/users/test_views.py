import pytest
from rest_framework.test import APIClient
from django.conf import settings
from rest_framework import status
from django.contrib.auth import get_user_model
from userprofile.models import UserProfile


@pytest.mark.django_db
def test_get_profile_api(client):

    client.defaults['SERVER_NAME'] = 'localhost'

    user = get_user_model().objects.create_user(
        username="testuser1",
        first_name="Test",
        last_name="User",
        email="testuser1@example.com",
        password="Password@123"
    )
    
    assert user.check_password("Password@123")  
    
    user_profile, created = UserProfile.objects.get_or_create(
        user=user,
        defaults={"profile_photo": "/profile_default.png", "gender": "Male", "place": "City"}
    )
    
    response = client.post('/api/auth/jwt/create/', data={'email': 'testuser1@example.com', 'password': 'Password@123'})
    assert response.status_code == status.HTTP_200_OK  
    token = response.data['access']  

    response = client.get(
        '/api/profile/me/', 
        HTTP_AUTHORIZATION=f'JWT {token}' 
    )
    print(response.data)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data["username"] == "testuser1"
    assert response.data["gender"] == "Other"
    assert response.data["place"] == None
    assert response.data["profile_photo"] == f"http://localhost{settings.MEDIA_URL}profile_default.png"


