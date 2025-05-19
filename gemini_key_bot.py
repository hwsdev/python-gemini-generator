#!/usr/bin/env python3
import os
import json
import subprocess
import random
import string
import time
from pathlib import Path
import argparse
import webbrowser

# Configuration
CONFIG_DIR = Path.home() / ".gemini"
CONFIG_FILE = CONFIG_DIR / "config.json"
PROJECT_PREFIX = "gemini-bot-"

def run_command(command):
    """Run a shell command and return the output"""
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"stderr: {e.stderr}")
        return None

def check_gcloud_installed():
    """Check if Google Cloud SDK is installed"""
    result = run_command("gcloud --version")
    return result is not None

def check_gcloud_auth():
    """Check if user is authenticated with gcloud"""
    result = run_command("gcloud auth list")
    return "No credentialed accounts" not in result

def random_project_id():
    """Generate a random project ID"""
    chars = string.ascii_lowercase + string.digits
    suffix = ''.join(random.choice(chars) for _ in range(6))
    return f"{PROJECT_PREFIX}{suffix}"

def create_project(project_id):
    """Create a new Google Cloud project"""
    print(f"Creating new Google Cloud project: {project_id}")
    result = run_command(f"gcloud projects create {project_id} --name=\"Gemini API Bot Project\"")
    if result is None:
        return False
    
    # Set as default project
    run_command(f"gcloud config set project {project_id}")
    return True

def enable_gemini_api(project_id):
    """Enable the Gemini API for the project"""
    print(f"Enabling Gemini API for project {project_id}")
    # The service name for Gemini API
    api_name = "generativelanguage.googleapis.com"
    result = run_command(f"gcloud services enable {api_name} --project={project_id}")
    return result is not None

def create_api_key(project_id):
    """Create an API key for the project"""
    print(f"Creating API key for project {project_id}")
    
    # Unfortunately, gcloud doesn't have a direct command to create API keys
    # We need to use the API or Cloud Console
    print("Opening Google Cloud Console to create an API key...")
    print("Please follow these steps:")
    print("1. In the Cloud Console, go to APIs & Services > Credentials")
    print("2. Click 'CREATE CREDENTIALS' and select 'API key'")
    print("3. Copy the generated API key")
    print("4. Return to this script and paste the key when prompted")
    
    # Open Cloud Console
    console_url = f"https://console.cloud.google.com/apis/credentials?project={project_id}"
    webbrowser.open(console_url)
    
    # Prompt user for the API key
    api_key = input("Paste your API key here: ").strip()
    return api_key if api_key else None

def save_config(project_id, api_key):
    """Save configuration to file"""
    CONFIG_DIR.mkdir(exist_ok=True)
    
    config = {
        "project_id": project_id,
        "api_key": api_key,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "auto_generated": True
    }
    
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"Configuration saved to {CONFIG_FILE}")
    return True

def show_usage_example(api_key):
    """Show an example of how to use the API key"""
    print("\n=== USAGE EXAMPLE ===")
    print("Here's how you can use your Gemini API key in Python:")
    print("\nimport requests")
    print("\n# API Key")
    print(f"API_KEY = '{api_key}'")
    print("\n# Endpoint")
    print("url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}'")
    print("\n# Request data")
    print("data = {")
    print("    'contents': [")
    print("        {")
    print("            'parts': [")
    print("                {")
    print("                    'text': 'Write a short poem about AI'")
    print("                }")
    print("            ]")
    print("        }")
    print("    ]")
    print("}")
    print("\n# Send request")
    print("response = requests.post(url, json=data)")
    print("print(response.json())")

def alternative_method():
    """Provide information on getting API key through AI Studio"""
    print("\n=== ALTERNATIVE METHOD ===")
    print("You can also get a Gemini API key through Google AI Studio:")
    print("1. Go to https://makersuite.google.com/app/apikey")
    print("2. Sign in with your Google account")
    print("3. Click 'Get API key'")
    print("4. Follow the prompts to create a new key")
    print("\nThis method is simpler and doesn't require gcloud setup.")
    
    open_ai_studio = input("Would you like to open AI Studio now? (y/n): ").lower().strip()
    if open_ai_studio == 'y':
        webbrowser.open("https://makersuite.google.com/app/apikey")

def main():
    parser = argparse.ArgumentParser(description="Google Gemini API Key Generator Bot")
    parser.add_argument("--use-ai-studio", action="store_true", help="Use Google AI Studio method instead of gcloud")
    args = parser.parse_args()
    
    if args.use_ai_studio:
        alternative_method()
        return
    
    print("===== Google Gemini API Key Generator Bot =====")
    
    # Check if gcloud is installed
    if not check_gcloud_installed():
        print("Google Cloud SDK (gcloud) is not installed or not in PATH.")
        print("Please install it from: https://cloud.google.com/sdk/docs/install")
        alternative_method()
        return
    
    # Check if user is authenticated
    if not check_gcloud_auth():
        print("You need to authenticate with Google Cloud first.")
        run_command("gcloud auth login")
        
        # Check again after authentication attempt
        if not check_gcloud_auth():
            print("Authentication failed. Try running 'gcloud auth login' manually.")
            alternative_method()
            return
    
    # Create a new project
    project_id = random_project_id()
    if not create_project(project_id):
        print("Failed to create a new project.")
        alternative_method()
        return
    
    # Enable the Gemini API
    if not enable_gemini_api(project_id):
        print("Failed to enable the Gemini API.")
        alternative_method()
        return
    
    # Wait for API enablement to propagate
    print("Waiting for API enablement to propagate (30 seconds)...")
    time.sleep(30)
    
    # Create API key
    api_key = create_api_key(project_id)
    if not api_key:
        print("No API key provided.")
        alternative_method()
        return
    
    # Save configuration
    save_config(project_id, api_key)
    
    # Show example
    show_usage_example(api_key)
    
    print("\n===== API Key Generation Complete =====")
    print(f"Your Gemini API Key: {api_key}")
    print(f"Google Cloud Project: {project_id}")
    print(f"Configuration saved to: {CONFIG_FILE}")

if __name__ == "__main__":
    main() 