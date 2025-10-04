from whyhow_api.config import Settings
import os

# Show environment
print("Environment variables:")
for key, value in os.environ.items():
    if "MONGO" in key:
        print(f"  {key}={value}")

# Create settings and show URI
settings = Settings()
print(f"\nGenerated URI: {settings.mongodb.uri}")
print(f"Host: {settings.mongodb.host}")
print(f"Database: {settings.mongodb.database_name}")
