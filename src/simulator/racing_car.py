class RacingCar(object):
    """Racing car"""
    def __init__(self, param):
        super(RacingCar, self).__init__()
        self.param = param

        self.pos = [0, 0]
        self.toward = [0, 0]
        self.speed = 0
        self.acce = 0  # Acceleration.
