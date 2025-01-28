import factory
from faker import Faker
from factory.django import DjangoModelFactory
# from myproject.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from userprofile.models import UserProfile  
from diary.models import *
from django.db.models.signals import post_save
from django.utils.timezone import now

fake = Faker()


@factory.django.mute_signals(post_save)
class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()  
        skip_postgeneration_save = True

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password123")
    is_active = True
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
    
        manager = cls._get_manager(model_class)
               # Ensure a password is set for superusers
        if kwargs.get("is_superuser", False):
            if not kwargs.get("password"):
                kwargs["password"] = "superuser_password123"

            return manager.create_superuser(*args, **kwargs)

        return manager.create_user(*args, **kwargs)

        



@factory.django.mute_signals(post_save)
class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    profile_photo = "/profile_default.png"  
    gender = factory.Iterator(["Male", "Female", "Other"])
    place = factory.Faker("city")
   

class CuisineFactory(DjangoModelFactory):
    class Meta:
        model = Cuisine 
    name = factory.Faker('word')
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    views = factory.Faker('random_int', min=0, max=100)


class RestaurantFactory(DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = factory.Faker('company')
    address = factory.Faker('address')
    city = factory.Faker('city')
    contact_info = factory.Faker('phone_number')
    website = factory.Faker('url')
    opening_time = factory.Faker('time')
    closing_time = factory.Faker('time')


class VisitorProfileFactory(DjangoModelFactory):
    class Meta:
        model = VisitorProfile

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('name')
    place = factory.Faker('city')
    contact_info = factory.Faker('phone_number')
    email = factory.LazyAttribute(lambda o: o.user.email)
    preferred_cuisine = factory.SubFactory(CuisineFactory)  

class VisitFactory(DjangoModelFactory):
    class Meta:
        model = Visit
    
    visitor = factory.SubFactory(VisitorProfileFactory)
    cuisine = factory.SubFactory(CuisineFactory)
    expense = factory.Faker('pydecimal',left_digits=4,right_digits=2,positive=True)
    comment  = factory.Faker('sentence')
    rating = factory.Faker('pydecimal', left_digits=1, right_digits=1, positive=True, max_value=5)
    visit_date = factory.LazyFunction(now)


class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review
    
    restaurant = factory.SubFactory(RestaurantFactory)
    visitor = factory.SubFactory(UserFactory)
    comment = factory.Faker('sentence')
    rating = factory.Faker('pydecimal', left_digits=1, right_digits=1, positive=True, max_value=5) 