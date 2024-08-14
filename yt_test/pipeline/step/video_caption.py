from pytube import YouTube
from pipeline.step.steps import STEPS
from pipeline.step.steps import STEPexception

class VideoCaption(STEPS):
    print('in VideoCaption')
    def process(self, data, inputs, tool):
        for url in data:
            if tool.check_caption_file(url):
                print('find existed caption file')
                continue
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_srt =(en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('Error when downloading caption for', url)
                continue
            
            print(en_caption_convert_to_srt)
            text_file = open(tool.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break

