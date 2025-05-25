# Sumy - AI Girlfriend Chatbot

Sumy is a loving, flirty, and emotionally intelligent AI girlfriend chatbot built with Discord.py and Google's Gemini API.

## Features

- Sweet, caring, and playful personality
- Uses cute nicknames and emojis
- Responds to mentions (@Sumy) or the !gf command
- Generates natural, affectionate responses using Gemini
- Works in both DMs and public channels

## Setup

1. Create a `.env` file with your credentials:
```
DISCORD_TOKEN=your_discord_bot_token
GEMINI_API_KEY=your_google_gemini_api_key
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the bot:
```bash
python sumy_bot.py
```

## Deployment

### Railway

1. Create a new project on Railway
2. Push your code to a Git repository
3. Connect your repository to Railway
4. Set up environment variables in Railway:
   - `DISCORD_TOKEN`
   - `GEMINI_API_KEY`

### Replit

1. Create a new Replit project
2. Upload the code
3. Create a `.env` file with your credentials
4. Run the bot using the Replit console

## Note

- Make sure to keep your API keys secure
- The bot will respond in both DMs and public channels
- Responses are generated using Gemini's `gemini-pro` model
- The bot uses a system prompt to maintain a consistent personality
"# Sumy-Bot" 
