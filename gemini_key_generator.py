#!/usr/bin/env python3
import os
import json
import argparse
import webbrowser
from pathlib import Path
import uuid
import datetime

def create_config_file(api_key=None):
    """Create a configuration file for the Gemini API key"""
    config = {
        "api_key": api_key or "",
        "created_at": datetime.datetime.now().isoformat(),
        "project_id": f"gemini-project-{uuid.uuid4().hex[:8]}"
    }
    
    config_dir = Path.home() / ".gemini"
    config_dir.mkdir(exist_ok=True)
    
    config_file = config_dir / "config.json"
    with open(config_file, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"Configuration file created at: {config_file}")
    return config_file

def open_cloud_console():
    """Open the Google Cloud Console to create an API key"""
    url = "https://console.cloud.google.com/apis/credentials"
    print(f"Opening {url} in your browser...")
    webbrowser.open(url)

def save_api_key(api_key):
    """Save the provided API key to the configuration file"""
    config_file = Path.home() / ".gemini" / "config.json"
    
    if config_file.exists():
        with open(config_file, "r") as f:
            config = json.load(f)
    else:
        config = {}
    
    config["api_key"] = api_key
    config["updated_at"] = datetime.datetime.now().isoformat()
    
    with open(config_file, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"API key saved to {config_file}")

def setup_instructions():
    """Display instructions for setting up a Google Gemini API key"""
    instructions = """
    === How to obtain a Google Gemini API Key ===
    
    1. Go to the Google AI Studio: https://makersuite.google.com/app/apikey
    2. Sign in with your Google account
    3. Click on "Get API key" 
    4. Choose "Create API key in new project" or use an existing project
    5. Copy the generated API key
    6. Run this tool with: python gemini_key_generator.py --save YOUR_API_KEY
    
    Alternatively, for Google Cloud Console method:
    1. Visit: https://console.cloud.google.com/
    2. Create a new project or select an existing one
    3. Enable the Gemini API for your project
    4. Go to APIs & Services > Credentials
    5. Click "Create credentials" and select "API key"
    6. Copy the generated key
    7. Run this tool with: python gemini_key_generator.py --save YOUR_API_KEY
    """
    print(instructions)

def get_api_key():
    """Get the current API key from the configuration file"""
    config_file = Path.home() / ".gemini" / "config.json"
    
    if not config_file.exists():
        print("No configuration file found.")
        return None
    
    with open(config_file, "r") as f:
        config = json.load(f)
    
    return config.get("api_key")

def main():
    parser = argparse.ArgumentParser(description="Google Gemini API Key Generator and Manager")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--init", action="store_true", help="Create initial configuration file")
    group.add_argument("--open-console", action="store_true", help="Open Google Cloud Console to create API key")
    group.add_argument("--save", metavar="API_KEY", help="Save the provided API key")
    group.add_argument("--get", action="store_true", help="Get the current API key")
    group.add_argument("--help-setup", action="store_true", help="Display setup instructions")
    
    args = parser.parse_args()
    
    if args.init:
        create_config_file()
    elif args.open_console:
        open_cloud_console()
    elif args.save:
        save_api_key(args.save)
    elif args.get:
        api_key = get_api_key()
        if api_key:
            print(f"Current API key: {api_key}")
        else:
            print("No API key found.")
    elif args.help_setup:
        setup_instructions()
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 