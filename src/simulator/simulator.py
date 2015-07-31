class Simulator(object):
    """Race simulator"""
    def __init__(self, sim_step, track, car, strategy):
        super(Simulator, self).__init__()
        self.sim_step = sim_step
        self.track = track
        self.car = car
        self.strategy = strategy

        self.time = 0
        self.view = None
        self.off_center = 0

    def step(self):
        """Simulate one step forward."""
        self.strategy.control(self.view, car)
        self.time += sim_step
