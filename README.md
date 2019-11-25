## Scalperr - Discord Bot
The Discord Bot which makes use of the Scalperr Backend API.

## Setup
`git clone git@github.com:carlzoo/scalperr-discord-bot.git`

`pip install requirements.txt`

## Testing
`manually only, currently not possible via CI build pipeline`

## Deployment
`python bot.py`

## Docker
Change `DISCORD_TOKEN` and `API_ACCESS_CODE` in Dockerfile.

Build container:

Go to project directory root and type

`docker image build -t scalperr-discord-bot:0.1 .`

`docker container run scalperr-discord-bot:0.1`