import server

server.app.config['TESTING'] = True
client = server.app.test_client()


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data

def test_mail_know():
    know_email = "admin@irontemple.com"
    response = client.post("/", data={'email': know_email})
    assert response.status_code == 200
    assert b'Points available:' in response.data

def test_mail_unknow():
    unknown_email = "mail@org.com"
    response = client.post("/", data={'email': unknown_email})
    assert response.status_code == 200
    assert b'Adresse email non autoris' in response.data

def test_no_email():
    no_email = ""
    response = client.post("/", data={'email': no_email})
    assert response.status_code == 200
    assert b'Veuillez saisir une adresse email !' in response.data

def test_logout():
    test_mail_know()
    response = client.get('/showSummary')
    assert response.status_code == 200  # With session, I acces Summary
    response = client.get('/logout')
    assert response.status_code == 302  # Logout redirect to login
    response = client.get('/showSummary')
    assert response.status_code == 302  # After Logout Session is destroy, I must do login

