#!/usr/bin/env python3
# 紫禁城完整布局 - 从零设计 (45 列 x 80 行)
import json
import os

COLS = 45
ROWS = 80
WALL = 0
FLOOR_1 = 1; FLOOR_2 = 2; FLOOR_3 = 3; FLOOR_4 = 4
FLOOR_5 = 5; FLOOR_6 = 6; FLOOR_7 = 7

COLORS = {
    'marble': {"h": 0, "s": 0, "b": 90, "c": 0},
    'stone': {"h": 0, "s": 0, "b": 55, "c": 0},
    'grass': {"h": 100, "s": 60, "b": 35, "c": 0},
    'courtyard': {"h": 30, "s": 30, "b": 65, "c": 0},
    'water': {"h": 210, "s": 70, "b": 45, "c": 0},
    'bridge': {"h": 0, "s": 0, "b": 95, "c": 0},
    'red_wall': {"h": 0, "s": 70, "b": 50, "c": 0},
    'gold_floor': {"h": 45, "s": 60, "b": 60, "c": 0},
}

tiles = [WALL] * (COLS * ROWS)
tileColors = [None] * (COLS * ROWS)

def idx(c, r): return r * COLS + c
def set_tile(c, r, tile, color=None):
    if 0 <= c < COLS and 0 <= r < ROWS:
        i = idx(c, r)
        tiles[i] = tile
        if color and color in COLORS: tileColors[i] = COLORS[color]

def set_rect(c1, r1, c2, r2, tile, color=None):
    for r in range(max(0, r1), min(ROWS, r2 + 1)):
        for c in range(max(0, c1), min(COLS, c2 + 1)):
            set_tile(c, r, tile, color)

def set_palace(c1, r1, c2, r2, floor_color='gold_floor'):
    set_rect(c1, r1, c2, r2, WALL, 'red_wall')
    set_rect(c1+1, r1+1, c2-1, r2-1, FLOOR_1, floor_color)

print("建造紫禁城...")
cx = COLS // 2  # 22

# 午门 (0-6)
print("  午门...")
set_palace(10, 0, 34, 6)
set_rect(21, 4, 23, 6, FLOOR_1, 'marble')

# 太和门广场 (7-14)
print("  太和门广场...")
set_rect(8, 7, 36, 14, FLOOR_4, 'courtyard')
set_rect(21, 7, 23, 14, FLOOR_1, 'marble')

# 太和门 (15-19)
print("  太和门...")
set_palace(12, 15, 32, 19)
set_rect(20, 17, 24, 19, FLOOR_2, 'stone')

# 金水河 (20-26, 弓形)
print("  金水河...")
for c in range(COLS):
    dist = abs(c - cx)
    if dist <= 14:
        arc = int(2 * (1 - (dist / 14) ** 2))
        rr = 23 - arc
        set_tile(c, rr, FLOOR_5, 'water')
        set_tile(c, rr+1, FLOOR_5, 'water')
        if rr > 0: set_tile(c, rr-1, FLOOR_3, 'grass')
        set_tile(c, rr+2, FLOOR_3, 'grass')

# 金水桥 (5 座)
print("  金水桥...")
for bx in [cx-10, cx-5, cx, cx+5, cx+10]:
    dist = abs(bx - cx)
    arc = int(2 * (1 - (dist / 14) ** 2))
    rr = 23 - arc
    for dx in [-1, 0, 1]:
        set_tile(bx+dx, rr, FLOOR_6, 'bridge')
        set_tile(bx+dx, rr+1, FLOOR_6, 'bridge')
set_rect(20, 20, 24, 26, FLOOR_1, 'marble')

# 太和殿广场 (27-34)
print("  太和殿广场...")
set_rect(6, 27, 38, 34, FLOOR_4, 'courtyard')
set_rect(21, 27, 23, 34, FLOOR_1, 'marble')

# 太和殿 (35-43)
print("  太和殿...")
set_palace(6, 35, 38, 43)
set_tile(cx, 39, WALL, 'red_wall')
set_tile(cx-1, 39, WALL, 'red_wall')
set_tile(cx+1, 39, WALL, 'red_wall')

# 中和殿 (44-48)
print("  中和殿...")
set_palace(14, 44, 30, 48)

# 保和殿 (49-55)
print("  保和殿...")
set_palace(10, 49, 34, 55)

# 乾清门 (56-60)
print("  乾清门...")
set_palace(14, 56, 30, 60)
set_rect(20, 58, 24, 60, FLOOR_2, 'stone')

# 乾清宫 (61-67)
print("  乾清宫...")
set_palace(10, 61, 34, 67)
set_tile(cx, 64, WALL, 'red_wall')

# 交泰殿 (68-71)
print("  交泰殿...")
set_palace(15, 68, 29, 71)

# 坤宁宫 (72-76)
print("  坤宁宫...")
set_palace(10, 72, 34, 76)

# 御花园 (77-79)
print("  御花园...")
set_rect(8, 77, 36, 79, FLOOR_3, 'grass')
# 堆秀山
for r in range(3):
    w = 3 - r
    set_rect(cx-w, 77-r, cx+w, 77-r, WALL, 'red_wall')
# 小路
for c in range(10, 35): set_tile(c, 78, FLOOR_2, 'stone')
set_tile(cx, 77, FLOOR_2, 'stone')
set_tile(cx, 79, FLOOR_2, 'stone')

# 东西六宫
print("  东西六宫...")
for r in [25, 35, 45]:
    set_palace(2, r, 10, r+5)   # 西
    set_palace(34, r, 42, r+5)  # 东

# 外墙
print("  外墙...")
for c in range(COLS):
    set_tile(c, 0, WALL, 'red_wall')
    set_tile(c, ROWS-1, WALL, 'red_wall')
for r in range(ROWS):
    set_tile(0, r, WALL, 'red_wall')
    set_tile(COLS-1, r, WALL, 'red_wall')

# 夹道
print("  夹道...")
for r in range(10, 75):
    set_tile(5, r, FLOOR_2, 'stone')
    set_tile(39, r, FLOOR_2, 'stone')

# 保存
layout = {
    "version": 1,
    "cols": COLS,
    "rows": ROWS,
    "tiles": tiles,
    "tileColors": tileColors,
    "furniture": []  # 必须有空数组，前端会迭代
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/layout.json')
with open(out, 'w') as f: json.dump(layout, f, indent=2)

print(f"\n✅ 紫禁城完成！{COLS}x{ROWS}={len(tiles)} tiles")
from collections import Counter
counts = Counter(tiles)
names = {0:'墙',1:'殿',2:'路',3:'草',4:'场',5:'水',6:'桥',7:'饰'}
for t, c in sorted(counts.items()): print(f"  {names.get(t,t)}: {c} ({c/len(tiles)*100:.1f}%)")
print(f"  颜色：{len([c for c in tileColors if c])}/{len(tileColors)}")
