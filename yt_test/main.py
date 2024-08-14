from pipeline.step.video_link import VideoLink
from pipeline.step.video_caption import VideoCaption
from pipeline.pipeline import Pipeline
from pipeline.step.preflight import Preflight
from pipeline.step.postflight import Postflight
from tools import Tools

def main():
    inputs = {
        #'channel_id': 'UCKSVUHI9rbbkXhvAXK-2uxA'
        'channel_id': 'UClvdIQwkgwMFwyjsDZoi-4g'
        }
    
    steps = [
        Preflight(),
        VideoLink(),
        VideoCaption(),
        Postflight(),
    ]

    tool = Tools()
    a = Pipeline(steps)
    a.run(inputs, tool)
    
if __name__ == '__main__':
    main()
    