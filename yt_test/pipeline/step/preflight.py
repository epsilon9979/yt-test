from pipeline.step.steps import STEPS

class Preflight(STEPS):
    def process(self, data, imputs, tool):
        print('in preflight')
        tool.create_dirs()