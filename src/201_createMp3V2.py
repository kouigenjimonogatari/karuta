from bs4 import BeautifulSoup
import json
import sys
import os
from pydub import AudioSegment
import argparse
import pandas as pd
from google.cloud import texttospeech

def synthesize_text(text, path, lang, sp_ja):
    """Synthesizes speech from the input string of text."""
    

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(ssml=text)

    language_code="en-US"
    name="en-US-Wavenet-D"

    if lang == "ja":
        language_code="ja-JP"
        name="ja-JP-Wavenet-B"

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=name,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate = sp_ja if lang == "ja" else 1.0
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open(path, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

inputPath = "data/genji.csv"

df = pd.read_csv(inputPath)

index2 = 0

for index, row in enumerate(df.itertuples()):
    index = row[0]

    if index < 15:
        continue

    text = row[3]

    if pd.isnull(text):
        continue

    index2 += 1

    outputPath = "../docs/audio/{}.mp3".format(str(index2).zfill(3))

    if os.path.exists(outputPath):
        continue

    spl = text.split(" ")
    
    
    ssml = '''
    <speak>
  {}
  <break time="400ms"/>{}<break time="400ms"/>
  {}
<break time="1200ms"/>
{}<break time="400ms"/>{}
</speak>
    '''.format(spl[0], spl[1], spl[2], spl[3], spl[4])

    

    synthesize_text(ssml, outputPath, "ja", 1.0)