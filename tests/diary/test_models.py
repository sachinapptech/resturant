import pytest
from diary.models import *
from tests.factories import *

@pytest.mark.django_db
def test_restaurant_average_rating():
    restaurant = RestaurantFactory()
    ReviewFactory.create_batch(3, restaurant=restaurant, rating=4.0)

    assert restaurant.average_rating() == 4.0
    assert restaurant.total_reviews() == 3


@pytest.mark.django_db
def test_visit_cuisines_ordered():
    visitor = VisitorProfileFactory()
    cuisines = CuisineFactory.create_batch(3)
    for cuisine in cuisines:
        VisitFactory(visitor=visitor,cuisine=cuisine)

    orderer_cuisines = Visit.cuisines_ordered(visitor)
    assert len(orderer_cuisines) == 3
    assert all(cuisine.name in orderer_cuisines for cuisine in cuisines)

@pytest.mark.django_db
def test_visitor_profile_autofill():
    user = VisitorProfileFactory().user
    profile = user.visitorprofile

    assert profile.name == user.get_full_name or user.username
    assert profile.email == user.email


@pytest.mark.django_db
def test_total_expenses():
    visitor = VisitorProfileFactory()
    VisitFactory.create_batch(5,visitor=visitor,expense=100)

    assert Visit.total_expenses(visitor) == 500

@pytest.mark.django_db
def test_resturant_str():
    restaurant = RestaurantFactory(name="Test Resturant")
    assert str(restaurant) == "Test Resturant"

@pytest.mark.django_db
def test_vivit_str():
    visit = VisitFactory()
    print(visit)
    assert str(visit) == f"Visit by {visit.visitor.name} on {visit.visit_date}"