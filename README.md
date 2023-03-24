# twitch-twitter-bot

An automated Twitter bot that tweets when a specified Twitch channel goes live or ends a stream. The bot is implemented using Python, Flask, the Twitch API, and the Twitter API.

## Features

- Real-time notifications using Twitch Webhooks
- Automated tweets when a stream starts or ends
- Easy to configure and deploy

## Prerequisites

- Python 3.6 or later
- A Twitch Developer account with a registered application
- A Twitter Developer account with API access
- A publicly accessible server for handling incoming webhook notifications (e.g., Heroku, PythonAnywhere)

## Installation

1. Clone this repository

2. Create a virtual environment and install dependencies

pip install -r requirements.txt

3. Update `config.py` with your API credentials and other settings


## Usage

1. Run the Flask server

By default, the server will start on port 5000. You can change the port in `app.py` if needed.

2. Subscribe to the Twitch "Stream Changed" webhook topic

You can run this code in a Python shell, or include it in a separate script to automate the subscription process.

3. The bot will now listen for incoming webhook notifications and send tweets when the specified Twitch channel goes live or ends a stream.



