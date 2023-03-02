import os
from google.cloud import translate_v2 as translate

# set up Google Cloud Translation client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/credentials.json"
translate_client = translate.Client()

# set the source and target languages
source_lang = 'de-CH'
target_lang = 'en-US'

# set the directory containing the text files to translate
directory_path = 'path/to/directory'

# iterate over the files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory_path, filename)
        
        # read the contents of the file
        with open(filepath, 'r') as file:
            text = file.read()
        
        # translate the text
        result = translate_client.translate(text, source_language=source_lang, target_language=target_lang)
        
        # write the translated text to a new file
        translated_filename = filename.split('.')[0] + '_translated.txt'
        translated_filepath = os.path.join(directory_path, translated_filename)
        with open(translated_filepath, 'w') as file:
            file.write(result['translatedText'])
