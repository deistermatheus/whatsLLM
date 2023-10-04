# WhatsLLM

A proof-of-concept integration between Twilio Whatsapp and OpenAI ChatGPT.

## Description

Most conversational commerce companies are interested in how new AI developments may improve end user experience.
This is a proof of concept project for using WhatsApp as an interface to OpenAI, allowing a customizable prompt and a short-term
memory. The project can be modified to include some more elaborate features, such as using embeddings for a custom knowledge base,
or integrating with other OpenAI features such as speech to text and image generation.

## Getting Started

### Prerequisites

* [Python 3.10](https://www.python.org/) - Check out [Libraries And Frameworks](#explore-libraries-and-frameworks)
* [Docker](https://www.docker.com/) - Package the app for deployment
* [SQL Database](https://neon.tech/) - Linked offering has a generous free tier
* [Twilio Account](https://www.twilio.com/docs) - First users get free credits
* [OpenAI API Key](https://openai.com/blog/openai-api) - First users get free credits
* [Ngrok](https://ngrok.com/) (or other network tunneling tool) for local development
* [Fly.io CLI](https://fly.io/docs/) - Free tier up to 3 apps, easily package and run Docker based applications

### Installing

* Clone this Repository
```sh
    git clone https://github.com/deistermatheus/whatsLLM.git
```

* Create an environment file, setting appropriate variables for Database, Twilio and OpenAI:

```sh
    cp .env.example .env
```

* Create the Database Structure

```sh
    alembic upgrade head
```

* Start the API

```sh
   uvicorn project.api.main:app --host 0.0.0.0 --reload
```

* Alternatively, to run a local docker image of the project:

```sh
    docker build -t whatsllm .
    docker run -it -p 8000:8000 --env-file=./.env whatsllm  bash server.sh
```

* Check the OpenAPI docs page or make a direct request to see the project is up and running:

```sh
   curl -X 'GET' \
  'http://localhost:8000/health' \
  -H 'accept: application/json'
```

* Setup your Twilio Webhook Endpoint

For local development, ngrok is recommended to get a public url for Twilio:

```sh
    ngrok http 8000
```

After obtaining a public URL, set up the Whatsapp Webhook in the Twilio Console. The 
docs for Twilio Webhooks can be found [here](https://www.twilio.com/docs/usage/webhooks/getting-started-twilio-webhooks).

## Deploying

To start the deployment process, a Fly.io account is required:

```sh
    fly launch
```

The app requires a database connection and API keys for integrations, to set required environment variables:

```sh
    fly secrets import < .env
```

After making changes:

```sh
    fly deploy
```

The app should now be available in a public url such as:

```sh
    https://<your-chosen-app-name>.fly.dev/health
    https://<your-chosen-app-name>.fly.dev/docs
```

### Deploying Automatically

Create a new secret in the repository with:

```sh
    fly tokens create deploy -x 99999h
```

Setup the [GitHub Action by defining a new repository secret](https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/) with the token

## Expected outcome

* Chat with the bot over Whatsapp, the following capture is using the Twilio Sandbox Number:
![sample-capture](https://github.com/deistermatheus/whatsLLM/assets/24402584/d2caa266-9888-41d9-831f-6939b245edd5)

## Mini Roadmap

### Features
- [x] Get the integration working
- [x] Add SQL Database for short term context
- [x] Save customizable prompt in chatbot configs
- [x] Deploy to the cloud
- [ ] Add Telegram as alternative channel
- [ ] Allow more customization choices over GPT (model, temperature...)
- [ ] Voice support
- [ ] Image generation
- [ ] Embeddings for larger context

### Code Quality

- [ ] Add Automated Testing with CI Check
- [ ] Improve OpenAPI documentation
- [ ] Improve Type Hinting
  
## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Explore Libraries and Frameworks

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [OpenAI SDK](https://github.com/openai/openai-python)
* [Twilio REST Client](https://www.twilio.com/docs/libraries/python)

## Acknowledgments
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
