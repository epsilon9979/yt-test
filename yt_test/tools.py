import os
from setting import DOWNLOAD
from setting import VIDEO
from setting import CAPTION

class Tools:
    def __init__(self):
        pass
    
    def create_dirs(self):
        os.makedirs(DOWNLOAD, exist_ok=True)
        os.makedirs(VIDEO, exist_ok=True)
        os.makedirs(CAPTION, exist_ok=True)
        
    def get_videolist_filepath(self,channel_id):
        return os.path.join(DOWNLOAD, channel_id+'.txt')
    
    def check_videolist_file(self, channel_id):
        path = self.get_videolist_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path)>0
    
    @staticmethod  
    def get_video_id(url):
        return url.split('watch?v=')[-1]
    
    def get_caption_filepath(self,url):
        return os.path.join(CAPTION, self.get_video_id(url) + '.txt')
    
    def check_caption_file(self,url):
        path = self.get_caption_filepath(url)
        return os.path.exists(path) and os.path.getsize(path)>0
    
  