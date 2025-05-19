#!/usr/bin/env python3
import os
import json
import time
import webbrowser
from pathlib import Path

# Configuration
CONFIG_DIR = Path.home() / ".gemini"
CONFIG_FILE = CONFIG_DIR / "config.json"

def generate_api_key():
    """Assist the user in generating an API key through Google AI Studio"""
    print("===== Gemini API Key Generator (AI Studio Method) =====")
    print("This script will help you get a Google Gemini API key through Google AI Studio.")
    
    # Open AI Studio
    print("\nOpening Google AI Studio in your web browser...")
    print("Please follow these steps:")
    print("1. Sign in with your Google account")
    print("2. Click on 'Get API key'")
    print("3. Choose to create a new API key")
    print("4. Copy the generated API key")
    print("5. Return to this script and paste the key when prompted")
    
    # Prompt user to continue
    input("\nPress Enter to open Google AI Studio...")
    webbrowser.open("https://makersuite.google.com/app/apikey")
    
    # Wait for user to get the API key
    print("\nWaiting for you to obtain your API key...")
    api_key = input("\nPaste your API key here: ").strip()
    
    if not api_key:
        print("No API key provided. Exiting.")
        return False
    
    # Save configuration
    save_config(api_key)
    return True

def save_config(api_key):
    """Save the API key to configuration file"""
    CONFIG_DIR.mkdir(exist_ok=True)
    
    config = {
        "api_key": api_key,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "method": "ai_studio"
    }
    
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"\nAPI key saved to {CONFIG_FILE}")

def show_usage_example(api_key):
    """Show an example of how to use the API key"""
    print("\n===== USAGE EXAMPLE =====")
    print("Here's a simple Python example to use your Gemini API key:")
    
    example = f'''
import requests

# Your API key
API_KEY = "{api_key}"

# API endpoint for Gemini Pro model
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

# Request data
data = {{
    "contents": [
        {{
            "parts": [
                {{
                    "text": "Write a short poem about programming"
                }}
            ]
        }}
    ]
}}

# Send request
response = requests.post(url, json=data)
result = response.json()

# Print response
print(result)
'''
    print(example)

def main():
    """Main function"""
    if generate_api_key():
        # Read the saved configuration
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
        
        api_key = config.get("api_key")
        
        print("\n===== API Key Generation Complete =====")
        print(f"Your Gemini API Key: {api_key}")
        
        # Show example
        show_usage_example(api_key)
        
        print("\nYou can now use this API key in your applications.")
        print("For testing, run: python test_gemini_api.py")

if __name__ == "__main__":
    main() 