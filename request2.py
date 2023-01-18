import requests
import pytest


# Submit a GET request to https://reqres.in/api/users/2
# Check that the response status code is equal to 200
def test_get_user_with_id_1_check_status_code_equals_200():
    res=requests.get("https://reqres.in/api/users/2")
    assert res.status_code==200


# Submit a GET request to https://reqres.in/api/users/2
# Check that the response header 'Content-Type' is equal to 'application/json; charset=utf-8'
def test_get_user_with_id_1_check_content_type_equals_json():
    res=requests.get("https://reqres.in/api/users/2")
    assert res.headers['Content-Type']=='application/json; charset=utf-8'


# Submit a GET request to https://reqres.in/api/users/2
# Check that the response body field 'data' exists
def test_get_user_with_id_1_check_name_field_exists():
    res=requests.get("https://reqres.in/api/users/2")
    resbody= res.json()
    assert 'data' in resbody


# Submit a GET request to https://reqres.in/api/users/2
# Check that the response body field 'name' has a value equal to 'Janet'
def test_get_user_with_id_1_check_name_equals_leanne_graham():
    res=requests.get("https://reqres.in/api/users/2")
    resbody= res.json()
    assert resbody['data']['first_name'] == 'Janet'



# Submit a GET request to https://reqres.in/api/users/2
# Check that the response body field 'data.email' has a value equal to 'janet.weaver@reqres.in'
def test_get_user_with_id_1_check_company_name_equals_romaguera_crona():
    res=requests.get("https://reqres.in/api/users/2")
    resbody= res.json()
    assert resbody['data']['email'] == 'janet.weaver@reqres.in'



# Submit a GET request to https://reqres.in/api/users?page=2
# Check that the response body is a list (an array) containing 10 elements
def test_get_all_users_check_number_of_users_equals_10():
     response = requests.get("https://reqres.in/api/users?page=2")
     response_body = response.json()
     assert len(response_body['data']) == 6




def test_delete():
     response = requests.delete("https://reqres.in/api/users/2")
     
     assert response.status_code == 204



def test_post():
     new_post = {
        "name": "developer",
        "job": "tester",
        
            }
     response = requests.post("https://reqres.in/api/users",json=new_post)
     
     assert response.status_code == 201
