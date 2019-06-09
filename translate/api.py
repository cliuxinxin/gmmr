from google.cloud import translate_v3beta1 as translate
client = translate.TranslationServiceClient()

project_id = 'api-project-692854300800'
text = '你好'
location = 'global'

parent = client.location_path(project_id, location)

response = client.translate_text(
    parent=parent,
    contents=[text],
    mime_type='text/plain',  # mime types: text/plain, text/html
    source_language_code='zh-CN',
    target_language_code='en-US')

for translation in response.translations:
    print('Translated Text: {}'.format(translation))