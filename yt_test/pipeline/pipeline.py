from pipeline.step.steps import STEPexception

class Pipeline:
    def __init__(self, which_step):
        self.steps= which_step
        
    def run(self,inputs,tool):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, tool)  #執行每一個步驟的程式功能
            except STEPexception as e:
                print('exception happened', e)
                break