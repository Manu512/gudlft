from random import randint
from locust import HttpUser, task, between



class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def show_summary(self):
        """ display tournament list """
        self.client.get("/showSummary")

    @task
    def book_get(self):
        """ display booking form """
        with self.client.get("/book/Spring%2520Festival/Iron Temple") as response:
            if response.elapsed.total_seconds() > 5:
                response.failure("Request took too long")
            elif response.status_code != 200:
                response.failure("Wrong Status Code")


    @task
    def purchase_post(self):
        self.client.post("/purchasePlaces", data={'club': 'Iron Temple',
                                                  'competition': 'Spring Festival',
                                                  'places': 1})

    @task
    def purchase_post_wrong_club(self):
        self.client.post("/purchasePlaces", data={'club': 'Simply Lift',
                                                  'competition': 'Spring Festival',
                                                  'places': 1})

    @task
    def book_get(self):
        competition = ['Fall%20Classic', 'Spring%20Festival']
        selected_competition = competition[randint(0, 1)]
        self.client.get("/book/{}/Iron%20Temple".format(selected_competition))


    @task
    def index_post(self):
        with self.client.get("/", catch_response=True) as response:
            if "Welcome" not in response.text:
                response.failure("Got wrong response")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("Request took too long")


    def on_start(self):
        """ login form / Initialize session"""
        self.client.post("/", data={"email": "admin@irontemple.com"})


    def on_quit(self):
        """ logout """
        self.client.get("/logout")
