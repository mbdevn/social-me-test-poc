"""
Centralized configuration for the SocialMe application.
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.debug = os.getenv('DEBUG', 'false').lower() == 'true'
        self.secret_key = os.getenv('SECRET_KEY', 'supersecretkey')
        self.claude_api_key = os.getenv('CLAUDE_API_KEY')
        self.port = int(os.getenv('PORT', 8004))
        self.db_uri = os.getenv('DB_URI', 'sqlite:///instance/socialme.db')
        self._extra = {
            'template_folder': os.getenv('TEMPLATE_FOLDER', 'templates'),
            'static_folder': os.getenv('STATIC_FOLDER', 'static'),
        }

    def get(self, key, default=None):
        return self._extra.get(key, default)

config = Config()
