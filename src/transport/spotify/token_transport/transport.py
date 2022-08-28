# STANDARD IMPORTS
import base64
import datetime

# THIRD PART IMPORTS
from decouple import config
import requests

# PROJECT IMPORTS
from src.domain.exceptions.exceptions import ClientSecretKeysNotProvided


class SpotifyAPI(object):
    token_url = config('SPOTIFY_TOKEN_URL')

    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expires = True

    def __init__(self, client_id: str, client_secret: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self) -> str:

        """return the base64 encoded string"""
        if self.client_secret is None and self.client_secret is None:
            raise ClientSecretKeysNotProvided

        client_credentials = f"{self.client_id}:{self.client_secret}"
        client_credentials_b64 = base64.b64encode(client_credentials.encode())
        return client_credentials_b64.decode()

    def get_token_header(self) -> dict:
        client_credential_b64 = self.get_client_credentials()

        token_header = {
            "Authorization": f"Basic {client_credential_b64}"
        }
        return token_header

    def get_token_data(self) -> dict:
        token_data = {
            "grant_type": "client_credentials"
        }
        return token_data

    def perform_auth(self):

        token_data = self.get_token_data()
        token_header = self.get_token_header()

        r = requests.post(
            config("SPOTIFY_TOKEN_URL"),
            data=token_data,
            headers=token_header
        )
        is_valid_requests = r.status_code in range(200, 299)

        if not is_valid_requests:
            return False

        data = r.json()
        now = datetime.datetime.now()
        access_token = data["access_token"]
        expire_in = data["expires_in"]

        expires = now + datetime.timedelta(seconds=expire_in)

        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expires = expires < now

        return True
