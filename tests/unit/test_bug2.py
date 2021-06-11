import conftest

club = 'Iron Temple'
place = 3
competition = 'Spring Festival'
email = "admin@irontemple.com"

def test_display_summary(clients):
    response = clients.post('/purchasePlaces', data={'club': club, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert "Welcome, " + email in str(response.data)
    assert b"Points available: 4" in response.data


def test_booking_not_exceed(clients):
    response = clients.post('/purchasePlaces', data={'club': club, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert b"Great-booking complete"


def test_booking_exceed(clients):
    place = 10
    response = clients.post('/purchasePlaces', data={'club': club, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert b"Waouhou ! booking incomplete !"


def test_thirteen_place_booking(clients):
    place = 13
    club = 'Simply Lift'
    response = clients.post('/purchasePlaces', data={'club': club, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert b"Booking incomplete ! 12 places maximum, subject to availability in your wallet"


def test_booking_empty(clients):
    place = ''
    club = 'Simply Lift'
    response = clients.post('/purchasePlaces', data={'club': club, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert b"Something went wrong-please try again"


def test_book_without_session(clients):
    response = clients.get('/book/{}/{}'.format(competition, club))
    assert response.status_code == 302
    assert "Redirecting" in str(response.data)


def test_book_with_session(clients):
    know_email = "admin@irontemple.com"
    response = clients.post('/', data={'email': know_email})
    response = clients.get('/book/{}/{}'.format(competition, club))
    assert response.status_code == 200
    assert competition in str(response.data)


def test_book_with_session_wrong_club(clients):
    know_email = "admin@irontemple.com"
    response = clients.post('/', data={'email': know_email})
    response = clients.get('/book/{}/{}'.format(competition, 'Simply Lift'))
    assert response.status_code == 302
    assert "You should be redirected automatically to target URL" in str(response.data)


def test_book_with_session_inexistant_club(clients):
    know_email = "admin@irontemple.com"
    response = clients.post('/', data={'email': know_email})
    response = clients.get('/book/{}/{}'.format(competition, 'Simply'))
    assert response.status_code == 302
    assert "You should be redirected automatically to target URL" in str(response.data)


