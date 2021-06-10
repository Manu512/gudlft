import conftest


club = 'Iron Temple'
place = 3
competition = 'Spring Festival'

def test_display_summary(clients):
    response = clients.post('/purchasePlaces', data={'club': club, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert b"Welcome, admin@irontemple.com" in response.data
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