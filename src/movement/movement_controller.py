class MovementController:
    def __init__(self, pokemon, screen_width: int, screen_height: int):
        self.pokemon = pokemon
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, dt: float):
        self.pokemon.x += self.pokemon.direction * self.pokemon.speed * dt

        if self.pokemon.x <= 0:
            self.pokemon.x = 0
            self.pokemon.direction = 1
            self.pokemon.state = "IDLE"

        if self.pokemon.x + self.pokemon.width >= self.screen_width:
            self.pokemon.x = self.screen_width - self.pokemon.width
            self.pokemon.direction = -1
            self.pokemon.state = "IDLE"

        if self.pokemon.state == "WALKING":
            self.pokemon.energy = max(0, self.pokemon.energy - 0.8 * dt)
