import os
from google.cloud import texttospeech
import io
import streamlit as st

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'

def synthesize_speech(text, lang='Japanese', gender='default'):
    gender_type = {
        'default': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
        'male': texttospeech.SsmlVoiceGender.MALE,
        'female': texttospeech.SsmlVoiceGender.FEMALE,
        'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
    }
    lang_code = {
        'English': 'en-US',
        'Japanese': 'ja-JP'
    }

    client = texttospeech.TextToSpeechClient()
    
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code[lang], ssml_gender=gender_type[gender]
    )
    
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response

# Streamlit app setup
st.title('Speech Synthesis App')

# Input data selection
input_option = st.selectbox('Select Input Data', ('Direct Input', 'Text File'))
input_data = None

if input_option == 'Direct Input':
    input_data = st.text_area('Enter text here.', 'Sample text for Cloud Speech-to-Text.')
else:
    uploaded_file = st.file_uploader('Upload a text file.', ['txt'])    
    if uploaded_file is not None:
        content = uploaded_file.read()
        input_data = content.decode()

if input_data is not None:
    st.write('Input Data')
    st.write(input_data)

    # Language and gender selection
    lang = st.selectbox('Select Language', ('Japanese', 'English'))
    gender = st.selectbox('Select Speaker Gender', ('default', 'male', 'female', 'neutral'))

    # Start speech synthesis
    if st.button('Start'):
        comment = st.empty()
        comment.write('Generating audio...')
        response = synthesize_speech(input_data, lang=lang, gender=gender)
        st.audio(response.audio_content)
        comment.write('Completed!')
