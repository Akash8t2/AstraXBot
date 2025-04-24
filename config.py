import os

# MongoDB URI
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://akashkashyap8t2:Akking8t2@cluster0.t3sbtoi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Telegram Bot Token
API_TOKEN = os.getenv("API_TOKEN", "your-bot-api-token-here")

# Bot Owner Details
OWNER_ID = 5397621246
OWNER_USERNAME = "@botcasx"

# Group and Channel Details
SUPPORT_GROUP = "https://t.me/BeatXFlowSupport"
COMMUNITY_CHANNEL = "https://t.me/BeatFlowCommunity"

# Logging
LOGGING_LEVEL = "INFO"  # Can be "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"

# MongoDB Collection
USER_COLLECTION = "users"  # MongoDB collection for storing user data

# Other settings (add more as required)
COMMAND_PREFIX = "!"  # Prefix for bot commands
