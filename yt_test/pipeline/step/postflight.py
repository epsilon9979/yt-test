from pipeline.step.steps import STEPS

class Postflight(STEPS):
    def process(self, data, imputs, tool):
        print('in postflight')