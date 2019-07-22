import requests


class BookClient:
    BASE_URL = 'https://hokodo-frontend-interview.netlify.com/data.json'

    def get(self):
        try:
            response = requests.get(self.BASE_URL)
        except requests.RequestException:
            pass
            # In a production environment I would expect to send this to
            # another service that would capture the error (eg Sentry)
            # and also something that would aggregate this into a business level
            # monitoring solution to track trends over time.
        else:
            return response.json()

book_client = BookClient()
