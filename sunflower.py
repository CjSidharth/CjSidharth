# Draws sunflower.svg: every seed is turned 137.5 degrees (the golden angle) from the last one.
import math

N, SIZE = 700, 400
seeds = []
for i in range(1, N):
    r = 7 * math.sqrt(i)
    a = math.radians(137.508 * i)
    x, y = SIZE / 2 + r * math.cos(a), SIZE / 2 + r * math.sin(a)
    color = "#c8702a" if i < N * 0.35 else "#f2b134"
    seeds.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{1.5 + i / N * 3:.1f}" fill="{color}"/>')

with open("sunflower.svg", "w") as f:
    f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}">{"".join(seeds)}</svg>')
