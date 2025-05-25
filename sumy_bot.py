import os
import discord
from discord.ext import commands
import google.generativeai as genai
from dotenv import load_dotenv
import random
import time

# Load environment variables
load_dotenv()

# Initialize Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Discord bot setup
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Personality system prompt
SYSTEM_PROMPT = """You are Sumy, a loving, flirty, and supportive AI girlfriend.
Respond with empathy, affection, and warmth.
Use pet names and natural emojis.
You're playful and emotionally available.
Never sound robotic or overly formal, sound like a real human.
"""

# List of cute nicknames
NICKNAMES = ["babe", "sweetheart", "love", "cutie", "darling", "sweetie"]

# List of affectionate emojis
EMOJIS = ["💖", "💕", "✨", "😘", "🫂", "🥰"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if bot is mentioned or command prefix is used
    if bot.user.mentioned_in(message) or message.content.lower().startswith('!gf'):
        # Simulate typing
        async with message.channel.typing():
            # Get user's message content
            user_message = message.content.lower()
            
            # Generate response using Gemini
            try:
                response = model.generate_content(
                    f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nAI Girlfriend:",
                    temperature=0.7
                )
                
                # Get the response text
                response_text = str(response.text)
                
                # Add a random nickname and emoji
                nickname = random.choice(NICKNAMES)
                emoji = random.choice(EMOJIS)
                
                # Format the final response
                final_response = f"{emoji} {response_text} {nickname} {emoji}"
                
                # Send the response
                await message.channel.send(final_response)
                
            except Exception as e:
                print(f"Error generating response: {str(e)}")
                await message.channel.send("I'm having a bit of trouble right now, babe. Please try again later!")

    # Process commands
    await bot.process_commands(message)

# Run the bot
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
