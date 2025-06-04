# Quorix
Quorix – Your ever-curious, voice-powered thinking companion that listens, remembers, and helps you untangle ideas like a genius rubber duck with a brain upgrade.


You'll need a Groq Cloud API key in order to run this.

In testing, it is able to achieve the following latencies:

- STT `whisper-large-v3-turbo`: 800ms
- LLM TTFT `llama-3.3-70b-versatile`: 200ms
- TTS `playai-tts`: 350ms

## Run agent in a console tab

1. `cd agent`
2. `python -m venv .venv`
3. `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `cp .env.example .env`
6. populate `.env` with valid values for keys
7. `python main.py dev`

## Run web client in another console tab

1. `cd client/web`
2. `pnpm i`
3. `cp .env.example .env.local`
4. populate `.env` with valid values for keys
5. `pnpm dev`

## Start the app

1. open a browser and navigate to `http://localhost:3000`