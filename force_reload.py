import sys
import importlib

# Remove ALL whyhow modules from cache
to_remove = [key for key in sys.modules.keys() if 'whyhow' in key]
for key in to_remove:
    del sys.modules[key]

# Now test
from whyhow_api.config import Settings
settings = Settings()
print(f"Generated URI: {settings.mongodb.uri}")
