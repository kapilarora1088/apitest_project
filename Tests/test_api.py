import requests
from config import  BASE_URI
from assertpy.assertpy import assert_that
from json import dumps


#GET /public-api/users-----------Postive testcases
def test_get_user():
    response = requests.get(BASE_URI)
    response_text = response.json()
    print(response_text)
    assert response.status_code == 200

#GET /public-api/users-----------Negative testcases
def test_get_user_negative():
    response = requests.get(BASE_URI+"/123")
    response_text = response.json()
    print(response_text['code'])
    assert_that(response_text['code']).is_equal_to(404)

#POST /public-api/users--------Negative testcases (Authentication failed)
def test_post_user():
    payload=dumps(
    {"id": 12345, "name": "Test Kaniyar", "email": "test@blick-gislason.biz", "gender": "male","status": "active"})
    headers={
        'Content-Type':'application/json',
        'Accept':'application/json'
    }
    response = requests.post(BASE_URI,data=payload,headers=headers)
    response_text = response.json()
    print(response.text)
    print(response_text['code'],response_text['data'])
    assert_that(response_text['code']).is_equal_to(401)

#GET /public-api/users/1234-----------Postive testcases
def test_get_user2():
    response = requests.get(BASE_URI + '/1234')
    response_text = response.json()
    print(response.text)
    print(response_text['code'])
    assert_that(response_text['code']).is_equal_to(200)

#PUT /public-api/users/123--------Negative testcases (Authentication failed)
def test_put_user():
    response = requests.put(BASE_URI+'/1234',data ={'name':'Test'})
    response_text= response.json()
    print(response.text)
    print(response_text['code'])
    assert_that(response_text['code']).is_equal_to(401)

#DELETE /public-api/users/123--------Negative testcases (Authentication failed)
def test_delete_user():
    response = requests.delete(BASE_URI+'/3661',data ={'name':'Test'})
    response_text= response.json()
    print(response.text)
    print(response_text['code'])
    assert_that(response_text['code']).is_equal_to(401)



