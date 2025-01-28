import pytest
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_user_serializer(user_factory, profile_factory):

    profile = profile_factory()
    user = profile.user

    serializer = UserSerializer(user)
    serialized_data = serializer.data

    # Assertions
    assert serialized_data["id"] == str(user.id)
    assert serialized_data["username"] == user.username
    assert serialized_data["email"] == user.email
    assert serialized_data["gender"] == profile.gender
    assert serialized_data["profile_photo"] == "/images/profile_default.png" 
    assert serialized_data["place"] == profile.place
    assert serialized_data["full_name"] == f"{user.first_name} {user.last_name}"


@pytest.mark.django_db
def test_user_serializer_superuser(user_factory):
    user = user_factory(is_superuser=True, is_staff=True,password="secure_password123")

    serializer = UserSerializer(user)
    serialized_data = serializer.data

    assert serialized_data["id"] == str(user.id)
    assert serialized_data["username"] == user.username
    assert serialized_data["email"] == user.email
    assert serialized_data["full_name"] == f"{user.first_name} {user.last_name}"
    assert serialized_data["admin"] is True

    # Verify password separately
    assert user.check_password("secure_password123")  