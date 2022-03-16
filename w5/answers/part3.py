import requests
import pytest

url = 'http://localhost:8080'

OK = 200

@pytest.fixture
def setup():
    requests.delete(f'{url}/clear')

def test_add_name(setup):
    response = requests.post(f'{url}/addnameage', json={
        'name': 'Rob', 'dob': 1000,
    })
    assert response.status_code == OK
    assert response.json() == {}

def test_get_names(setup):
    response = requests.get(f'{url}/getnamesages')
    assert response.status_code == OK
    assert response.json() == []

    requests.post(f'{url}/addnameage', json={
        'name': 'Rob', 'dob': 1000,
    })

    response = requests.get(f'{url}/getnamesages')
    assert response.status_code == OK
    assert response.json() == [{
        'name': 'Rob', 'age': 51,
    }]

def test_get_names_restrict(setup):
    requests.post(f'{url}/addnameage', json={
        'name': 'Rob', 'dob': 1000,
    })
    requests.post(f'{url}/addnameage', json={
        'name': 'Hayden', 'dob': 10 ** 8,
    })

    response = requests.get(f'{url}/getnamesages', params={'min_age': 50})
    assert response.status_code == OK
    assert response.json() == [{
        'name': 'Rob', 'age': 51,
    }]

def test_edit_names_ages(setup):
    requests.post(f'{url}/addnameage', json={
        'name': 'Rob', 'dob': 1000,
    })

    response = requests.put(f'{url}/editnameage', json={
        'name': 'Rob', 'dob': 10 ** 8,
    })

    response = requests.get(f'{url}/getnamesages')
    assert response.status_code == OK
    assert response.json() == [{
        'name': 'Rob', 'age': 48,
    }]