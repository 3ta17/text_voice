# Speech Synthesis App

This is a simple speech synthesis application built using Python's `streamlit` and Google Cloud's Text-to-Speech API. The app allows users to input text and convert it into spoken audio in multiple languages and genders.

---

## Features

- **Text-to-Speech Conversion**: 
  Converts input text into an audio file using Google Cloud's Text-to-Speech service.
- **Language Selection**: 
  Supports Japanese (`ja-JP`) and English (`en-US`).
- **Gender Selection**: 
  Offers a choice of speaker gender: male, female, neutral, or default.
- **Input Options**: 
  - Direct text input
  - Text file upload

---

## Requirements

- **Python**: 3.6 or higher
- **Dependencies**:
  - `google-cloud-texttospeech`
  - `streamlit`

---

## Setup Instructions

1. **Install Dependencies**:
   Run the following command to install required packages:
   ```bash
   pip install google-cloud-texttospeech streamlit
