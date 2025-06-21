import os
import streamlit as st
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
import googleapiclient.discovery
import json

def get_google_auth_flow():
    """
    Initializes and returns the Google OAuth flow.
    This function uses the client_secrets.json file, which contains the application's
    OAuth 2.0 client ID and client secret. This file does NOT contain user credentials.
    It identifies the application to Google's authentication servers, allowing users
    to sign in with their own Google accounts.
    """
    client_secrets_path = os.path.join("src", "main", "config", "credentials.json")
    if not os.path.exists(client_secrets_path):
        st.error("Credentials file not found. Please add credentials.json to src/main/config")
        return None

    flow = Flow.from_client_secrets_file(
        client_secrets_path,
        scopes=['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/userinfo.profile', 'openid'],
        redirect_uri='http://localhost:8501'
    )
    return flow

def get_auth_url(flow):
    """Generates the authorization URL for Google OAuth."""
    auth_url, _ = flow.authorization_url(prompt='consent') # prompt='consent' can be removed for one time permission request.
    return auth_url

def get_credentials(flow, code):
    """Fetches the credentials after the user has authorized the app."""
    flow.fetch_token(code=code)
    return flow.credentials

def get_user_info(credentials):
    """Fetches user information using the provided credentials."""
    user_info_service = googleapiclient.discovery.build('oauth2', 'v2', credentials=credentials)
    user_info = user_info_service.userinfo().get().execute()
    return user_info

def credentials_to_json(credentials):
    """Converts a credentials object to a JSON string for storing in session state."""
    return credentials.to_json()

def credentials_from_json(json_str):
    """Converts a JSON string from session state back to a credentials object."""
    info = json.loads(json_str)
    return Credentials(**info) 