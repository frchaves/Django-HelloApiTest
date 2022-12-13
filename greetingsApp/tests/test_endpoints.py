import pytest

from django.urls import reverse
from greetingsApp.models import Greetings


@pytest.mark.django_db
def test_list_greetings(client):
    """"
    Test the list/GET endpoint for greetings.
    """
    Greetings.objects.create(name="John", number_greetings=1)
    url = reverse("greetings-list")
    response = client.get(url)
    assert response.status_code == 200
    assert response.data[0]["name"] == "John"
    assert response.data[0]["number_greetings"] == 1


@pytest.mark.parametrize("expected_result", [{'Hello,John'}])
@pytest.mark.django_db
def test_post_greetings(client, expected_result):
    """"
    Test the create/POST endpoint for greetings.
    """
    url = reverse("greetings-list")
    response = client.post(url, {"name": "John"})
    assert response.status_code == 200
    assert response.data == expected_result
    test_greetings = Greetings.objects.filter(name="John")[0]
    assert test_greetings.number_greetings == 1

