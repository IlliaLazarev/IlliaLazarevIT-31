import math

NAME = "Illia Lazarev"
GROUP = "IT-31"

# Розміри кімнати (метри)
LENGTH = 4.2
WIDTH = 3.5
HEIGHT = 2.7

# Розміри дверей
DOOR_WIDTH = 0.9
DOOR_HEIGHT = 2.0

# Розміри вікна
WINDOW_WIDTH = 1.4
WINDOW_HEIGHT = 1.5

# Плитка
TILE_LENGTH = 0.3
TILE_WIDTH = 0.3
TILE_PRICE = 42.30

print(f"{NAME}, {GROUP}")

# 1. Площа підлоги
floor_area = LENGTH * WIDTH

# Площа стін
wall_area = 2 * (LENGTH + WIDTH) * HEIGHT

# Площа дверей і вікна
door_area = DOOR_WIDTH * DOOR_HEIGHT
window_area = WINDOW_WIDTH * WINDOW_HEIGHT

wall_area -= door_area + window_area

# 2. Діагоналі
floor_diagonal = math.hypot(LENGTH, WIDTH)

room_diagonal = math.dist(
    (0, 0, 0),
    (LENGTH, WIDTH, HEIGHT)
)

# 3. Кількість плиток
tile_area = TILE_LENGTH * TILE_WIDTH

tiles_exact = floor_area / tile_area

print(f"room: {LENGTH} x {WIDTH} x {HEIGHT} m")
print(f"floor area: {floor_area:.2f} m2")
print(f"wall area: {wall_area:.2f} m2")
print(f"floor diag: {floor_diagonal:.2f} m")
print(f"room diag: {room_diagonal:.2f} m")

print(f"\ntiles exact: {tiles_exact:.2f}")
print(f"  round: {round(tiles_exact)}")
print(f"  floor: {math.floor(tiles_exact)}")
print(f"  ceil: {math.ceil(tiles_exact)}")

tiles_to_buy = math.ceil(tiles_exact * 1.10)

print(f"tiles to buy: {tiles_to_buy} (+10% spare)")

# 4. Кількість фарби
paint_liters = wall_area * 2 / 10
paint_cans = math.ceil(paint_liters / 2.5)

print(f"paint: {paint_liters:.2f} l")
print(f"paint cans: {paint_cans}")

# 5. Вартість плитки двома способами
cost_multiplication = tiles_to_buy * TILE_PRICE

cost_addition = 0

for _ in range(tiles_to_buy):
    cost_addition += TILE_PRICE

print(f"\ntiles cost: {cost_multiplication:.2f} UAH")
print(f"sum == mul: {cost_addition == cost_multiplication}")
print(f"isclose: {math.isclose(cost_addition, cost_multiplication)}")
print(f"difference: {abs(cost_addition - cost_multiplication)}")
