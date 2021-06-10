import server

server.app.config['TESTING'] = True
client = server.app.test_client()


def test_index():
    landing = client.get("/")
    assert landing.status_code == 200


def test_mail_know():
    know_email = "admin@irontemple.com"
    response = client.post("/showSummary", data={'email': know_email})
    assert response.status_code == 200


def test_mail_unknow():
    unknown_email = "mail@org.com"
    response = client.post("/showSummary", data={'email': unknown_email})
    assert response.status_code == 302


def test_no_email():
    no_email = ""
    response = client.post("/showSummary", data={'email': no_email})
    assert response.status_code == 302
