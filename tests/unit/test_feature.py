import conftest

club1 = 'Iron Temple'
email1 = "admin@irontemple.com"
club2 = 'Simply Lift'
email2 = 'john@simplylift.co'
place = 5
competition = 'Fall Classic2'


def test_competition_booking_message(clients):
    response = clients.post('/purchasePlaces', data={'club': club2, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert b"Welcome, john@simplylift.co" in response.data
    assert b"Great-booking complete ! You have reserved 5 places" in response.data

    response = clients.post('/purchasePlaces', data={'club': club1, 'competition': competition, 'places': place - 2})
    assert b"Welcome, admin@irontemple.com" in response.data
    assert b"Booking incomplete ! We are sorry, the competition is full !" in response.data
