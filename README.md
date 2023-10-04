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
* UNIX system
* Python 3.10
* SQL Database
* Twilio Account 
* OpenAI API Key

#### Optional
* Docker and Docker Compose

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

```
    ngrok http 8000
```

### Expected outcome

* Chat with the bot over Whatsapp, the following capture is using the Twilio Sandbox Number:
![sample-capture](https://github.com/deistermatheus/whatsLLM/assets/24402584/d2caa266-9888-41d9-831f-6939b245edd5)

  

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
