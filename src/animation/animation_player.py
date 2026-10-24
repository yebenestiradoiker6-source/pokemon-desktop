class AnimationPlayer:
    def __init__(self, frames=None, fps=8, loop=True):
        self.frames = frames or []
        self.fps = fps
        self.loop = loop
        self.frame_index = 0
        self.frame_time = 0.0
        self.frame_duration = 1.0 / fps

    def update(self):
        if not self.frames:
            return

        self.frame_time += self.frame_duration
        if self.frame_time >= self.frame_duration:
            self.frame_time = 0.0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                if self.loop:
                    self.frame_index = 0
                else:
                    self.frame_index = len(self.frames) - 1

    def current_frame(self):
        if not self.frames:
            return None
        return self.frames[self.frame_index]

    def set_frames(self, frames):
        self.frames = frames
        self.frame_index = 0
        self.frame_time = 0.0
