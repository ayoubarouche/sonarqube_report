class Measure : 
    def __init__(self,
                metric=None,
                 value=None,
                 best_value=None,
                 period = None):
        self.metric = metric 
        self.value = value 
        self.best_value = best_value
        self.period = period

    def parse_jsonMetric(self,json_str):
        if 'metric' in json_str:
            self.metric=json_str['metric']
        if 'value' in json_str:
            self.value=json_str['value']
        if 'bestValue' in json_str:
            self.best_value=json_str['bestValue']
        if 'period' in json_str:
            self.period = json_str['period']