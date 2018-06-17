################################################################################
#### Filename: 		'main_test.py'
#### Written by:	Andrew St. Pierre
#### Last modified:	Jun-17-2018
################################################################################

import webtest

import main


def test_get():
    app = webtest.TestApp(main.app)

    response = app.get('/')

    assert response.status_int == 200
    assert response.body == 'Hello, World!'
