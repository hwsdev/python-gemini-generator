# Google Gemini API Key Generator

A simple Python tool to help you generate, manage, and test Google Gemini API keys.

## Installation

1. Make sure you have Python 3.6+ installed.
2. Install the required dependencies:

```bash
pip install requests
```

## Usage

### Setting Up Your API Key

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