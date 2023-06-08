from gtts import gTTS
from io import BytesIO, BufferedRandom
import speech_recognition as sr
from pydub import AudioSegment




# конвертр text to voice

def converter_text_to_voice(text: str) -> BytesIO:
    bytes_file = BytesIO()
    audio = gTTS(text=text, lang='ru')
    audio.write_to_fp(bytes_file)
    bytes_file.seek(0)
    return bytes_file


# конвертр voice to text
def converter_voice_to_text(voice_path: str) -> str:
    recognizer = sr.Recognizer()
    with sr.AudioFile(voice_path) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="ru")
        return text



# конвертр ogg в wav
def converter_ogg_to_wav(filename: str, file: BytesIO) -> BufferedRandom:
    path = filename.split("/")
    name = path[-1].split(".ogg")
    converted_path = name[0] + '.wav'
    segment = AudioSegment.from_ogg(file)
    wav_file = segment.export(converted_path, format="wav")
    return wav_file