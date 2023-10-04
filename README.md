# WhatsLLM

A proof-of-concept integration between Twilio Whatsapp and OpenAI ChatGPT.

## Description

Most conversational commerce companies are interested in how new AI developments may improve end user experience.
This is a proof of concept project for using WhatsApp as an interface to OpenAI, allowing a customizable prompt and a short-term
memory. The project can be modified to include some more elaborate features, such as using embeddings for a custom knowledge base,
or integrating with other OpenAI features such as speech to text and image generation.

## Getting Started

### Dependencies

#### Required
* [Python 3.10](https://www.python.org/)
* [SQL Database](https://neon.tech/) - Linked offering has a generous free tier
* [Twilio Account](https://www.twilio.com/docs) - First users get free credits
* [OpenAI API Key](https://openai.com/blog/openai-api) - First users get free credits
* [Ngrok](https://ngrok.com/) (or other network tunneling tool) for local development

#### Optional
* Docker and Docker Compose - Helps with deployment and running the project using a local SQL database

### Installing

* Clone this Repository
```sh
    git clone https://github.com/deistermatheus/whatsLLM.git
```

* Setup the environment variables
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

* Setup your Twilio Webhook Endpoint

For local development, ngrok is recommended:

```sh
    ngrok http 8000
```

* Check the OpenAPI docs page or make a direct request to see the project is up and running:

```sh
    curl -X 'GET' \
  'http://localhost:8000/health' \
  -H 'accept: application/json'
```

### Expected outcome

* Chat with the bot over Whatsapp, the following capture is using the Twilio Sandbox Number:
![sample-capture](https://github.com/deistermatheus/whatsLLM/assets/24402584/d2caa266-9888-41d9-831f-6939b245edd5)

  
## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
* [awesome-readme](https://github.com/matiassingers/awesome-readme)

## Explore Libraries and Frameworks

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [OpenAI SDK](https://github.com/openai/openai-python)
* [Twilio REST Client](https://www.twilio.com/docs/libraries/python)

