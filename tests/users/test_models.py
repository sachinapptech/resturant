import pytest
from django.core.exceptions import ValidationError

def test_user_str(base_user):
    assert base_user.__str__() == f"{base_user.username}"

def test_user_short_name(base_user):
    short_name = f"{base_user.username}"
    assert base_user.get_short_name() == short_name


def test_user_full_name(base_user):
    full_name = f"{base_user.first_name.title()} {base_user.last_name.title()}"
    assert base_user.get_full_name == full_name    

@pytest.mark.django_db
def test_base_user_email_is_normalized(user_factory):
    email = "jessica89@example.org"
    user = user_factory.create(email=email)  
    assert user.email == email.lower() 
    
def test_super_user_is_not_staff(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True,is_staff=False)
    assert str(err.value) == "Superuser must have is_staff=True"


def test_super_user_is_not_superuser(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(email = None)
    assert str(err.value) == 'Base User Account: An email address is required'

def test_create_user_with_no_username(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == "User must submit a username"

def test_create_user_with_no_firstname(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "User must submit a first name"

def test_create_user_with_no_lastname(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "User must submit a last name"


def test_create_superuser_with_no_email(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None,is_superuser=True,is_staff=True)
    assert str(err.value) == "Admin User Account: An email address is required"


def test_create_superuser_with_no_password(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None,is_superuser=True,is_staff=True)
    assert str(err.value) == "Superusers must have a password"

def test_user_email_incorrect(user_factory):
    
    with pytest.raises(ValidationError) as err:
        user_factory.create(email="sachin9958soni")  
    assert err.value.messages[0] == "You must provide a valid email address"