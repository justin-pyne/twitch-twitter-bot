import requests
import config

def get_twitch_token():
    url = 'https://id.twitch.tv/oauth2/token'
    payload = {
        'client_id': config.TWITCH_CLIENT_ID,
        'client_secret': config.TWITCH_CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, data=payload)
    return response.json()['access_token']

def subscribe_to_twitch_webhook(channel_id, callback_url, oauth_token):
    url = 'https://api.twitch.tv/helix/eventsub/subscriptions'
    headers = {
        'Client-ID': config.TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {oauth_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'type': 'stream.online',
        'version': '1',
        'condition': {
            'broadcaster_user_id': channel_id
        },
        'transport': {
            'method': 'webhook',
            'callback': callback_url,
        }
    }
