# Google Gemini API Key Generator

A simple Python tool to help you generate, manage, and test Google Gemini API keys.

## Installation

1. Make sure you have Python 3.6+ installed.
2. Install the required dependencies:

```bash
pip install requests
```

3. (Optional) For automated API key generation, install the Google Cloud SDK:
   - Download from: https://cloud.google.com/sdk/docs/install
   - Follow the installation instructions for your platform
   
## Usage

### Automatic API Key Generation (New!)

#### Method 1: Simple AI Studio Key Generator (Recommended)

The simplest way to get a Gemini API key is through Google AI Studio:

```bash
python ai_studio_key_generator.py
```

This script will:
1. Open Google AI Studio in your browser
2. Guide you through the process of creating an API key
3. Save the API key to your config file
4. Show a usage example

#### Method 2: Google Cloud SDK Method

For more advanced users, you can use the bot script to automatically create a Google Cloud project and generate an API key:

```bash
python gemini_key_bot.py
```

This will:
1. Check if Google Cloud SDK is installed
2. Authenticate with your Google account
3. Create a new project
4. Enable the Gemini API
5. Guide you through API key creation
6. Save the key to your configuration file

For a simpler alternative method using Google AI Studio:

```bash
python gemini_key_bot.py --use-ai-studio
```

### Manual API Key Management

1. Initialize the configuration file:

```bash
python gemini_key_generator.py --init
```

2. To get instructions on how to obtain a Google Gemini API key:

```bash
python gemini_key_generator.py --help-setup
```

3. Open the Google Cloud Console to create an API key:

```bash
python gemini_key_generator.py --open-console
```

4. Once you have your API key, save it:

```bash
python gemini_key_generator.py --save YOUR_API_KEY
```

5. To view your current API key:

```bash
python gemini_key_generator.py --get
```

### Testing Your API Key

After setting up your API key, you can test if it works with the Gemini API:

```bash
python test_gemini_api.py
```

This will send a simple test prompt to the Gemini API and display the response.

## Notes

- API keys are stored locally in `~/.gemini/config.json`
- The actual API key generation is done through the Google Cloud Console or Google AI Studio
- This tool helps manage and test your API keys, not create them directly

## Requirements

- Python 3.6+
- `requests` library

## License

MIT 