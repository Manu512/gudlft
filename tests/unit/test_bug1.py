import conftest


def test_index(clients):
    response = clients.get("/")
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data


def test_mail_know(clients):
    know_email = "admin@irontemple.com"
    response = clients.post("/", data={'email': know_email})
    assert response.status_code == 200
    assert b'Points available:' in response.data


def test_mail_unknow(clients):
    unknown_email = "mail@org.com"
    response = clients.post("/", data={'email': unknown_email})
    assert response.status_code == 200
    assert b'Adresse email non autoris' in response.data


def test_no_email(clients):
    no_email = ""
    response = clients.post("/", data={'email': no_email})
    assert response.status_code == 200
    assert b'Veuillez saisir une adresse email !' in response.data


def test_logout(clients):
    test_mail_know(clients)
    response = clients.get('/showSummary')
    assert response.status_code == 200  # With session, I acces Summary
    response = clients.get('/logout')
    assert response.status_code == 302  # Logout redirect to login
    response = clients.get('/showSummary')
    assert response.status_code == 302  # After Logout Session is destroy, I must do login
