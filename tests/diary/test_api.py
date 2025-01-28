import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

client = APIClient()

@pytest.mark.django_db
def test_create_user_simplejwt():
    payload = {
        "username": "sachin",
        "first_name": "Soni",
        "last_name": "Soni",
        "email": "sachin99589soni@gmail.com",
        "password": "Helloworld@123456",
        "re_password":"Helloworld@123456",
    }
    
    response = client.post("/api/auth/users/", payload)
    assert response.status_code == 201
    assert response.data["email"] == payload["email"]



