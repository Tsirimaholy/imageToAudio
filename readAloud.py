from PIL import Image
import pyttsx3
import pytesseract


def to_audio(text_to_read, audio_output):
    """This function convert textual data into audio

    Args:
        text_to_read (str): The textual data to be converted into audio
        audio_output (str): The name of the audio output file
    """
    
    speaker = pyttsx3.init()
    # read aloud voice the texteual data
    speaker.say(text_to_read)
    # save it in a audio file 
    speaker.save_to_file(text_to_read, f'{audio_output}.mp3')
    speaker.runAndWait()


# path to executable binary of tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\Administrator\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

# The path of the image to recognize text on
image_path = input("The image path > ")
img = Image.open(image_path)

# convert recognized text from the image to txt
image_to_txt = pytesseract.image_to_string(img)

# prompt for the audio output
audio_output = input('output file without extension 🔉> ')
to_audio(image_to_txt, audio_output)
