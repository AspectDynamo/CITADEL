class BacktestEngine:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data
        self.results = []

    def run(self):
        for event in self.data:
            self.execute_strategy(event)

    def execute_strategy(self, event):
        signal = self.strategy.get_signal(event)
        self.results.append(signal)
        self.log_results(event, signal)

    def log_results(self, event, signal):
        # Log execution results
        print(f'Event: {event}, Signal: {signal}')