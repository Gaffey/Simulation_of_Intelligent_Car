import math

class TrackPart(object):
    """Part of a racing track"""
    def __init__(self, index, prev_track, next_track):
        super(TrackPart, self).__init__()
        self.index = index
        self.prev_track = prev_track
        self.next_track = next_track


class StraightTrack(TrackPart):
    """Straight track"""
    def __init__(self, index, start_pos, end_pos, prev_track=None,
                                                  next_track=None):
        super(StraightTrack, self).__init__(index, prev_track, next_track)
        self.start_pos = start_pos
        self.end_pos = end_pos

    @property
    def length(self):
        return math.sqrt((start_pos[0] - end_pos[0]) ** 2 +
                         (start_pos[1] - end_pos[1]) ** 2);

class CurveTrack(TrackPart):
    """Curve track"""
    def __init__(self, index, center, radius, start_degree, end_degree,
                 prev_track=None, next_track=None):
        super(CurveTrack, self).__init__(index, prev_track, next_track)
        self.index = index
        self.center = center
        self.radius = radius
        self.start_degree = start_degree
        self.end_degree = end_degree

    @property
    def start_pos(self):
        pass

    @property
    def end_pos(self):
        pass

    @property
    def length(self):
        pass


class RacingTrack(object):
    """Racing track"""
    def __init__(self):
        super(RacingTrack, self).__init__()
        self.parts = []
