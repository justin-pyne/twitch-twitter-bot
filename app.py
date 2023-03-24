import hashlib
import hmac
from flask import Flask, request, abort, jsonify
from twitter_api import send_tweet
import config

app = Flask(__name__)

@app.route('/twitch-webhook', methods=['GET', 'POST'])
def twitch_webhook():
    if request.method == 'GET':
        challenge = request.args.get('hub.challenge')
        return jsonify({'hub.challenge': challenge})
    elif request.method == 'POST':
        # Verify request signature
        signature = request.headers.get('Twitch-Eventsub-Message-Signature')
        secret = config.WEBHOOK_SECRET.encode()
        message_id = request.headers.get('Twitch-Eventsub-Message-Id')
        timestamp = request.headers.get('Twitch-Eventsub-Message-Timestamp')
        body = request.data.decode()

        expected_signature = hmac.new(secret, f'{message_id}{timestamp}{body}'.encode(), hashlib.sha256).hexdigest()
        if signature != f'{"sha256="}{expected_signature}':
            abort(403)

        # Process webhook data
        data = request.json
        event = data['event']
        user_name = event['broadcaster_user_name']
        type = event['type']

        if type == 'live':
            # Tweet that the stream has started
            send_tweet(f'{user_name} is now live on Twitch! Check it out: https://www.twitch.tv/{user_name}')
        elif type == 'offline':
            # Tweet that the stream has ended
            send_tweet(f'{user_name} has just ended their Twitch stream. Catch them next time! https://www.twitch.tv/{user_name}')

        return '', 204

if __name__ == '__main__':
    app.run()
