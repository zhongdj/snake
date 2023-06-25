import random

class Snake:
    def __init__(self, x, y, size, length):
        self.size = size
        self.segments = [(x, y)]
        for i in range(length - 1):
            self.segments.append((x - size * (i + 1), y))
        self.direction = "right"

    def move(self):
        x, y = self.segments[0]
        if self.direction == "up":
            y -= self.size
        elif self.direction == "down":
            y += self.size
        elif self.direction == "left":
            x -= self.size
        elif self.direction == "right":
            x += self.size
        self.segments.pop()
        self.segments.insert(0, (x, y))

    def grow(self):
        x, y = self.segments[0]
        if self.direction == "up":
            y -= self.size
        elif self.direction == "down":
            y += self.size
        elif self.direction == "left":
            x -= self.size
        elif self.direction == "right":
            x += self.size
        self.segments.insert(0, (x, y))

    def check_collision(self, screen_width, screen_height):
        x, y = self.segments[0]
        if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
            return True
        for segment in self.segments[1:]:
            if segment == self.segments[0]:
                return True
        return False

class Food:
    def __init__(self, screen_width, screen_height, size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.size = size
        self.position = None

    def place(self):
        x = random.randint(0, self.screen_width // self.size - 1) * self.size
        y = random.randint(0, self.screen_height // self.size - 1) * self.size
        self.position = (x, y)
