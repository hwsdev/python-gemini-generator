#!/usr/bin/env python3
import os
import json
from pathlib import Path
import requests

def get_api_key():
    """Get the API key from the configuration file"""
    config_file = Path.home() / ".gemini" / "config.json"
    
    if not config_file.exists():
        print("No configuration file found. Please run gemini_key_generator.py --init first.")
        return None
    
    with open(config_file, "r") as f:
        config = json.load(f)
    
    api_key = config.get("api_key")
    if not api_key:
        print("No API key found in the configuration file.")
        print("Please run: python gemini_key_generator.py --help-setup")
        return None
    
    return api_key

def test_gemini_api(prompt="Tell me a short joke about programming"):
    """Test the Gemini API with a simple prompt"""
    api_key = get_api_key()
    if not api_key:
        return
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }
    
    print(f"Sending request to Gemini API with prompt: '{prompt}'")
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            
            # Extract the response text
            if "candidates" in result and len(result["candidates"]) > 0:
                candidate = result["candidates"][0]
                if "content" in candidate and "parts" in candidate["content"]:
                    parts = candidate["content"]["parts"]
                    text = "".join(part.get("text", "") for part in parts)
                    print("\nAPI Response:")
                    print("-" * 50)
                    print(text)
                    print("-" * 50)
                    return True
            
            print("Unexpected response format:", result)
            
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Exception occurred: {e}")
    
    return False

if __name__ == "__main__":
    print("Testing Gemini API connection...")
    test_gemini_api() 