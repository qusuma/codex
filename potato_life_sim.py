import math
import random
import sys
from dataclasses import dataclass

import pygame


WIDTH, HEIGHT = 800, 600
FPS = 60

BG_COLOR = (161, 212, 255)
FLOOR_COLOR = (241, 223, 193)
UI_PANEL = (28, 38, 57)
TEXT_COLOR = (245, 247, 252)
ACCENT = (255, 205, 93)
GREEN = (117, 225, 122)
RED = (255, 105, 105)


@dataclass
class Zone:
    name: str
    rect: pygame.Rect
    label: str
    color: tuple


class FloatingText:
    def __init__(self, text, pos, color=(255, 255, 255)):
        self.text = text
        self.x, self.y = pos
        self.life = 1.2
        self.color = color

    def update(self, dt):
        self.y -= 35 * dt
        self.life -= dt

    def draw(self, surface, font):
        alpha = max(0, min(255, int(255 * (self.life / 1.2))))
        text = font.render(self.text, True, self.color)
        text.set_alpha(alpha)
        surface.blit(text, (self.x, self.y))


class Sparkle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(40, HEIGHT - 140)
        self.speed = random.uniform(18, 40)
        self.radius = random.randint(1, 3)
        self.brightness = random.randint(150, 255)

    def update(self, dt):
        self.y -= self.speed * dt
        if self.y < 30:
            self.y = HEIGHT - 120
            self.x = random.randint(0, WIDTH)

    def draw(self, surface):
        pygame.draw.circle(surface, (self.brightness, self.brightness, 255), (int(self.x), int(self.y)), self.radius)


class Potato:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2 + 50
        self.vx = 0
        self.vy = 0
        self.speed = 220
        self.facing_right = True
        self.blink_timer = random.uniform(1.5, 3.5)
        self.blink_duration = 0.12
        self.is_blinking = False
        self.animation_t = 0

    @property
    def rect(self):
        return pygame.Rect(int(self.x - 32), int(self.y - 42), 64, 84)

    def update(self, dt, keys):
        self.vx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed
        self.vy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * self.speed
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.x = max(30, min(WIDTH - 30, self.x))
        self.y = max(95, min(HEIGHT - 86, self.y))

        if self.vx > 0:
            self.facing_right = True
        elif self.vx < 0:
            self.facing_right = False

        moving = abs(self.vx) + abs(self.vy) > 0
        self.animation_t += dt * (7 if moving else 2.5)

        self.blink_timer -= dt
        if self.blink_timer <= 0 and not self.is_blinking:
            self.is_blinking = True
            self.blink_timer = self.blink_duration
        elif self.is_blinking and self.blink_timer <= 0:
            self.is_blinking = False
            self.blink_timer = random.uniform(1.7, 4.0)

    def draw(self, surface):
        bob = math.sin(self.animation_t) * 2

        # Shadow
        shadow_w = 44 + int(abs(math.sin(self.animation_t * 0.7) * 4))
        pygame.draw.ellipse(surface, (130, 101, 77), (self.x - shadow_w // 2, self.y + 38, shadow_w, 12))

        body_color = (194, 143, 92)
        outline = (120, 84, 50)
        cheek = (245, 160, 182)

        body_rect = pygame.Rect(self.x - 32, self.y - 44 + bob, 64, 84)
        pygame.draw.ellipse(surface, body_color, body_rect)
        pygame.draw.ellipse(surface, outline, body_rect, 3)

        # Arms
        arm_offset = math.sin(self.animation_t * 1.5) * 2
        left_arm = (self.x - 36, self.y - 6 + arm_offset)
        right_arm = (self.x + 36, self.y - 6 - arm_offset)
        pygame.draw.circle(surface, body_color, left_arm, 8)
        pygame.draw.circle(surface, outline, left_arm, 8, 2)
        pygame.draw.circle(surface, body_color, right_arm, 8)
        pygame.draw.circle(surface, outline, right_arm, 8, 2)

        # Feet
        foot_y = self.y + 34 + bob
        step = math.sin(self.animation_t * 2) * 2
        pygame.draw.ellipse(surface, (133, 94, 58), (self.x - 20, foot_y + step, 16, 10))
        pygame.draw.ellipse(surface, (133, 94, 58), (self.x + 4, foot_y - step, 16, 10))

        # Face
        eye_y = self.y - 12 + bob
        eye_dx = 12 if self.facing_right else -12

        if self.is_blinking:
            pygame.draw.line(surface, (47, 32, 24), (self.x - 12 + eye_dx * 0.15, eye_y), (self.x - 4 + eye_dx * 0.15, eye_y), 3)
            pygame.draw.line(surface, (47, 32, 24), (self.x + 4 + eye_dx * 0.15, eye_y), (self.x + 12 + eye_dx * 0.15, eye_y), 3)
        else:
            pygame.draw.circle(surface, (40, 23, 19), (int(self.x - 8 + eye_dx * 0.15), int(eye_y)), 4)
            pygame.draw.circle(surface, (40, 23, 19), (int(self.x + 8 + eye_dx * 0.15), int(eye_y)), 4)
            pygame.draw.circle(surface, (255, 255, 255), (int(self.x - 7 + eye_dx * 0.15), int(eye_y - 1)), 1)
            pygame.draw.circle(surface, (255, 255, 255), (int(self.x + 9 + eye_dx * 0.15), int(eye_y - 1)), 1)

        pygame.draw.arc(surface, (58, 33, 23), (self.x - 10, self.y + 2 + bob, 20, 12), math.radians(10), math.radians(170), 2)
        pygame.draw.circle(surface, cheek, (int(self.x - 16), int(self.y + 2 + bob)), 5)
        pygame.draw.circle(surface, cheek, (int(self.x + 16), int(self.y + 2 + bob)), 5)


class LifeSimGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Spud Life: Chibi Potato Sim")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.title_font = pygame.font.SysFont("verdana", 28, bold=True)
        self.ui_font = pygame.font.SysFont("verdana", 18)
        self.small_font = pygame.font.SysFont("verdana", 14)

        self.potato = Potato()
        self.floaters = []
        self.sparkles = [Sparkle() for _ in range(36)]

        self.day = 1
        self.clock_minutes = 8 * 60
        self.time_speed = 5.0
        self.weather = random.choice(["Sunny", "Cloudy", "Breezy"])
        self.season = random.choice(["Spring", "Summer", "Autumn"])

        self.hunger = 78.0
        self.energy = 82.0
        self.happiness = 75.0
        self.hygiene = 74.0
        self.coins = 22

        self.event_timer = 20.0
        self.message = "Welcome home, tiny spud! Explore and press E to interact."
        self.message_time = 6.0

        self.minigame_active = False
        self.minigame_timer = 0.0
        self.snacks = []
        self.minigame_score = 0
        self.minigame_goal = 8

        self.zones = [
            Zone("Kitchen", pygame.Rect(55, 125, 165, 145), "Cook / Eat", (255, 190, 140)),
            Zone("Desk", pygame.Rect(585, 125, 165, 145), "Work", (153, 192, 255)),
            Zone("Bath", pygame.Rect(55, 340, 165, 145), "Shower", (170, 245, 232)),
            Zone("Bed", pygame.Rect(585, 340, 165, 145), "Sleep", (211, 172, 255)),
            Zone("Park", pygame.Rect(315, 425, 170, 95), "Play Mini-Game", (180, 255, 172)),
        ]

    def post_message(self, text, duration=4.0):
        self.message = text
        self.message_time = duration

    def add_floater(self, text, color=(255, 255, 255)):
        self.floaters.append(FloatingText(text, (self.potato.x - 12, self.potato.y - 60), color=color))

    def clamp_stats(self):
        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))
        self.happiness = max(0, min(100, self.happiness))
        self.hygiene = max(0, min(100, self.hygiene))

    def stat_decay(self, dt):
        self.hunger -= 1.8 * dt
        self.energy -= 1.2 * dt
        self.hygiene -= 0.95 * dt
        self.happiness -= 0.65 * dt

        if self.hunger < 20:
            self.energy -= 0.9 * dt
            self.happiness -= 0.85 * dt
        if self.energy < 20:
            self.happiness -= 0.75 * dt
        if self.hygiene < 20:
            self.happiness -= 0.7 * dt

        self.clamp_stats()

    def update_time(self, dt):
        self.clock_minutes += dt * self.time_speed
        if self.clock_minutes >= 24 * 60:
            self.clock_minutes -= 24 * 60
            self.day += 1
            bonus = random.randint(4, 9)
            self.coins += bonus
            self.happiness += 3
            self.post_message(f"A fresh day begins! You found {bonus} bonus coins.")

    def maybe_random_event(self, dt):
        self.event_timer -= dt
        if self.event_timer > 0:
            return
        self.event_timer = random.uniform(20, 34)

        event_roll = random.random()
        if event_roll < 0.30:
            self.coins += 6
            self.happiness += 4
            self.add_floater("+6 coins", ACCENT)
            self.post_message("A neighbor tipped you for your adorable smile! +6 coins")
        elif event_roll < 0.58:
            self.energy += 7
            self.add_floater("+7 energy", GREEN)
            self.post_message("You took a mindful breathing break. Energy restored.")
        elif event_roll < 0.78:
            loss = random.randint(3, 7)
            self.coins = max(0, self.coins - loss)
            self.happiness -= 5
            self.add_floater(f"-{loss} coins", RED)
            self.post_message("Oops! You bought a novelty hat for your pet pebble.")
        else:
            self.happiness += 8
            self.add_floater("+8 joy", (255, 160, 235))
            self.post_message("A tiny rainbow appeared! Your potato heart feels full.")
        self.clamp_stats()

    def start_minigame(self):
        self.minigame_active = True
        self.minigame_timer = 18.0
        self.minigame_score = 0
        self.snacks = []
        for _ in range(13):
            self.snacks.append([random.randint(80, WIDTH - 80), random.randint(120, HEIGHT - 100), random.randint(0, 2)])
        self.post_message("Park game started! Collect snacks before time runs out.")

    def interact(self):
        zone_hit = None
        for zone in self.zones:
            if self.potato.rect.colliderect(zone.rect):
                zone_hit = zone
                break

        if zone_hit is None:
            self.post_message("No interaction nearby. Walk into a room and press E!")
            return

        name = zone_hit.name
        if name == "Kitchen":
            if self.hunger < 80 and self.coins >= 3:
                self.hunger += 28
                self.happiness += 4
                self.coins -= 3
                self.add_floater("Yum! +hunger", GREEN)
                self.post_message("You cooked fluffy butter noodles. Delicious!")
            elif self.coins < 3:
                self.post_message("Need 3 coins for ingredients.")
            else:
                self.post_message("You're already quite full.")

        elif name == "Desk":
            reward = 8 if self.energy > 25 else 4
            self.coins += reward
            self.energy -= 10
            self.hygiene -= 4
            self.happiness -= 2
            self.add_floater(f"+{reward} coins", ACCENT)
            self.post_message("You did cozy remote work and earned coins.")

        elif name == "Bath":
            self.hygiene += 34
            self.happiness += 5
            self.energy -= 4
            self.add_floater("Fresh!", (140, 250, 255))
            self.post_message("Bubble bath complete. Squeaky clean spud!")

        elif name == "Bed":
            self.energy += 36
            self.hunger -= 8
            self.clock_minutes += 100
            self.add_floater("Zzz...", (205, 205, 255))
            self.post_message("You took a cozy nap.")

        elif name == "Park":
            if not self.minigame_active:
                self.start_minigame()

        self.clamp_stats()

    def update_minigame(self, dt):
        if not self.minigame_active:
            return

        self.minigame_timer -= dt
        p = self.potato.rect
        collected = []
        for idx, (sx, sy, kind) in enumerate(self.snacks):
            if p.collidepoint(sx, sy):
                collected.append(idx)
                self.minigame_score += 1
                self.happiness += 2
                self.energy -= 1
                self.add_floater("snack!", (255, 220, 150))

        for i in reversed(collected):
            self.snacks.pop(i)

        if not self.snacks and self.minigame_timer > 0:
            self.minigame_timer = 0

        if self.minigame_timer <= 0:
            self.minigame_active = False
            earned = self.minigame_score + (5 if self.minigame_score >= self.minigame_goal else 0)
            self.coins += earned
            if self.minigame_score >= self.minigame_goal:
                self.happiness += 12
                self.post_message(f"Amazing run! Score {self.minigame_score}. Bonus coins awarded.")
            else:
                self.post_message(f"Mini-game over! Score {self.minigame_score}. You still earned {earned} coins.")
            self.clamp_stats()

    def draw_background(self):
        self.screen.fill(BG_COLOR)
        pygame.draw.rect(self.screen, FLOOR_COLOR, (0, 90, WIDTH, HEIGHT - 90))

        # Windows + sky strip
        pygame.draw.rect(self.screen, (140, 197, 255), (0, 0, WIDTH, 90))
        for i in range(4):
            x = 60 + i * 190
            pygame.draw.rect(self.screen, (240, 248, 255), (x, 18, 130, 56), border_radius=10)
            pygame.draw.rect(self.screen, (96, 148, 217), (x + 5, 23, 120, 46), border_radius=8)

        # Zone decorations
        for zone in self.zones:
            pygame.draw.rect(self.screen, zone.color, zone.rect, border_radius=18)
            pygame.draw.rect(self.screen, (80, 80, 90), zone.rect, 2, border_radius=18)
            text = self.small_font.render(zone.label, True, (37, 37, 45))
            self.screen.blit(text, (zone.rect.x + 10, zone.rect.y + 10))

        if self.minigame_active:
            for sx, sy, kind in self.snacks:
                if kind == 0:
                    c = (255, 194, 120)
                elif kind == 1:
                    c = (255, 145, 165)
                else:
                    c = (255, 230, 132)
                pygame.draw.circle(self.screen, c, (sx, sy), 9)
                pygame.draw.circle(self.screen, (140, 90, 50), (sx, sy), 9, 2)

        for sparkle in self.sparkles:
            sparkle.draw(self.screen)

    def draw_ui(self):
        panel = pygame.Rect(12, HEIGHT - 118, WIDTH - 24, 106)
        pygame.draw.rect(self.screen, UI_PANEL, panel, border_radius=16)
        pygame.draw.rect(self.screen, (75, 91, 126), panel, 2, border_radius=16)

        title = self.title_font.render("Spud Life", True, ACCENT)
        self.screen.blit(title, (24, HEIGHT - 110))

        hh = int(self.clock_minutes // 60)
        mm = int(self.clock_minutes % 60)
        time_text = f"Day {self.day}  {hh:02d}:{mm:02d}  •  {self.weather}, {self.season}"
        self.screen.blit(self.ui_font.render(time_text, True, TEXT_COLOR), (24, HEIGHT - 78))

        coins_text = self.ui_font.render(f"Coins: {self.coins}", True, (255, 234, 132))
        self.screen.blit(coins_text, (24, HEIGHT - 52))

        stats = [
            ("Hunger", self.hunger, (255, 162, 118)),
            ("Energy", self.energy, (146, 195, 255)),
            ("Happiness", self.happiness, (255, 147, 218)),
            ("Hygiene", self.hygiene, (160, 250, 235)),
        ]

        start_x = 250
        for i, (name, value, color) in enumerate(stats):
            x = start_x + i * 130
            y = HEIGHT - 88
            self.screen.blit(self.small_font.render(name, True, TEXT_COLOR), (x, y))
            pygame.draw.rect(self.screen, (57, 67, 85), (x, y + 20, 105, 12), border_radius=8)
            pygame.draw.rect(self.screen, color, (x, y + 20, int(105 * (value / 100)), 12), border_radius=8)

        hint = "Move: Arrow Keys / WASD  •  Interact: E  •  Quit: ESC"
        if self.minigame_active:
            hint = f"Mini-game: collect snacks! Time {self.minigame_timer:04.1f}s  Score {self.minigame_score}"
        self.screen.blit(self.small_font.render(hint, True, (220, 229, 250)), (250, HEIGHT - 52))

        if self.message_time > 0:
            msg = self.ui_font.render(self.message, True, TEXT_COLOR)
            box = msg.get_rect(center=(WIDTH // 2, 28))
            bg = box.inflate(16, 10)
            pygame.draw.rect(self.screen, (32, 45, 66), bg, border_radius=10)
            pygame.draw.rect(self.screen, (74, 101, 144), bg, 2, border_radius=10)
            self.screen.blit(msg, box)

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_e:
                        self.interact()

            keys = pygame.key.get_pressed()
            key_proxy = {
                pygame.K_LEFT: keys[pygame.K_LEFT] or keys[pygame.K_a],
                pygame.K_RIGHT: keys[pygame.K_RIGHT] or keys[pygame.K_d],
                pygame.K_UP: keys[pygame.K_UP] or keys[pygame.K_w],
                pygame.K_DOWN: keys[pygame.K_DOWN] or keys[pygame.K_s],
            }

            self.potato.update(dt, key_proxy)

            self.update_time(dt)
            self.stat_decay(dt)
            self.maybe_random_event(dt)
            self.update_minigame(dt)

            if self.message_time > 0:
                self.message_time -= dt

            for sparkle in self.sparkles:
                sparkle.update(dt)

            for floater in self.floaters:
                floater.update(dt)
            self.floaters = [f for f in self.floaters if f.life > 0]

            # Lose condition soft-recovery
            if self.energy <= 0 or self.hunger <= 0:
                self.energy = max(12, self.energy)
                self.hunger = max(12, self.hunger)
                self.happiness = max(20, self.happiness - 6)
                self.clock_minutes += 75
                self.post_message("You fainted from exhaustion! Time skipped, take better care.", duration=5.0)

            self.draw_background()
            self.potato.draw(self.screen)
            for floater in self.floaters:
                floater.draw(self.screen, self.small_font)
            self.draw_ui()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    try:
        LifeSimGame().run()
    except Exception as exc:
        pygame.quit()
        print(f"Game exited with error: {exc}")
        sys.exit(1)
