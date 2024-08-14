import urllib.request
import json

from setting import api
from pipeline.step.steps import STEPS
from pipeline.step.steps import STEPexception

class VideoLink(STEPS):
    print('in VideoLink')
    def process(self, data, inputs, tool):
        channel_id = inputs['channel_id']
        if tool.check_videolist_file(channel_id):
            print('find existed videolist file for channel_id', channel_id)
            return self.read_file(tool.get_videolist_filepath(channel_id))
            
        api_key = api
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

        video_links = []
        url = first_url
        while True:
            try:
                inp = urllib.request.urlopen(url)
                resp = json.load(inp)
            except:
                raise STEPexception

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break
        print(video_links[1:3])
        self.write_to_file(video_links, tool.get_videolist_filepath(channel_id))
        return video_links[1:3]

    def write_to_file(self, video_links, file_path):
        with open(file_path, 'w')as f:
            for url in video_links:
                f.write(url+'\n')
                
    def read_file(self, file_path):
        video_links=[]
        with open(file_path, 'r') as f:
            for url in f:
                video_links.append(url.strip())
        return video_links