#!/usr/bin/env python3
# 紫禁城布局优化 v3 - 添加 tileColors 配置
# 草地 = 绿色，金水河 = 蓝色

import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_dir, 'data/layout.json'), 'r') as f:
    layout = json.load(f)

cols = layout['cols']  # 45
rows = layout['rows']  # 80
tiles = layout['tiles']

# 初始化 tileColors（和 tiles 一样长）
tileColors = layout.get('tileColors', None)
if tileColors is None or len(tileColors) != len(tiles):
    tileColors = [None] * len(tiles)

# Tile 类型
WALL = 0
FLOOR_1 = 1
FLOOR_2 = 2
FLOOR_3 = 3  # 草地 → 绿色
FLOOR_4 = 4
FLOOR_5 = 5  # 金水河 → 蓝色
FLOOR_6 = 6
FLOOR_7 = 7

# 颜色配置 (HSL)
GREEN_GRASS = {"h": 100, "s": 60, "b": 35, "c": 0}      # 绿色草地
BLUE_WATER = {"h": 210, "s": 70, "b": 45, "c": 0}       # 蓝色河水
GRAY_STONE = {"h": 0, "s": 0, "b": 50, "c": 0}          # 灰色石板路
LIGHT_MARBLE = {"h": 0, "s": 0, "b": 85, "c": 0}        # 浅色汉白玉

def idx(col, row):
    return row * cols + col

def set_tile(col, row, tile_type, color=None):
    if 0 <= col < cols and 0 <= row < rows:
        i = idx(col, row)
        tiles[i] = tile_type
        if color:
            tileColors[i] = color

def set_rect(col1, row1, col2, row2, tile_type, color=None):
    for r in range(row1, min(row2 + 1, rows)):
        for c in range(col1, min(col2 + 1, cols)):
            i = idx(c, r)
            tiles[i] = tile_type
            if color:
                tileColors[i] = color

print("开始紫禁城布局优化 v3（带颜色配置）...")

# 1. 铺设草地（东西六宫区域）- FLOOR_3 + 绿色
print("  铺设草地...")
set_rect(5, 15, 25, 40, FLOOR_3, GREEN_GRASS)
set_rect(20, 15, 40, 40, FLOOR_3, GREEN_GRASS)

# 2. 绘制内金水河（太和殿前，弓形）- FLOOR_5 + 蓝色
print("  绘制金水河...")
center_x = cols // 2
river_row_base = 48
arc_height = 3

for x in range(cols):
    dist = abs(x - center_x)
    if dist <= 18:
        arc_offset = int(arc_height * (1 - (dist / 18) ** 2))
        river_row = river_row_base - arc_offset
        
        set_tile(x, river_row, FLOOR_5, BLUE_WATER)
        set_tile(x, river_row + 1, FLOOR_5, BLUE_WATER)
        
        # 河岸草地
        if river_row > 0:
            set_tile(x, river_row - 1, FLOOR_3, GREEN_GRASS)
        set_tile(x, river_row + 2, FLOOR_3, GREEN_GRASS)

# 3. 金水桥（5 座汉白玉桥）- FLOOR_1 + 浅色
print("  建造金水桥...")
bridge_positions = [center_x - 12, center_x - 6, center_x, center_x + 6, center_x + 12]

for bx in bridge_positions:
    dist = abs(bx - center_x)
    arc_offset = int(arc_height * (1 - (dist / 18) ** 2))
    river_row = river_row_base - arc_offset
    
    for dx in [-1, 0, 1]:
        set_tile(bx + dx, river_row, FLOOR_1, LIGHT_MARBLE)
        set_tile(bx + dx, river_row + 1, FLOOR_1, LIGHT_MARBLE)

# 4. 御花园
print("  建造御花园...")
# 堆秀山（假山）
hill_x, hill_y = center_x, 6
for r in range(4):
    width = 4 - r
    set_rect(hill_x - width, hill_y - r, hill_x + width, hill_y - r, WALL)

# 御花园草地
set_rect(10, 2, 35, 12, FLOOR_3, GREEN_GRASS)

# 古树位置
tree_positions = [
    (10, 4), (15, 3), (30, 3), (35, 4),
    (8, 8), (37, 8),
    (10, 11), (18, 10), (27, 10), (35, 11),
]
for tx, ty in tree_positions:
    set_tile(tx, ty, WALL)

# 亭子
set_rect(13, 5, 16, 7, FLOOR_1, LIGHT_MARBLE)
set_rect(29, 5, 32, 7, FLOOR_1, LIGHT_MARBLE)

# 御花园小路
for c in range(10, 36):
    set_tile(c, 9, FLOOR_2, GRAY_STONE)
for r in range(0, 13):
    set_tile(center_x, r, FLOOR_2, GRAY_STONE)

# 5. 中轴线石板路
print("  铺设中轴线石板路...")
for r in range(13, 60):
    set_tile(center_x - 1, r, FLOOR_2, GRAY_STONE)
    set_tile(center_x, r, FLOOR_2, GRAY_STONE)
    set_tile(center_x + 1, r, FLOOR_2, GRAY_STONE)

# 6. 宫殿装饰
print("  添加宫殿装饰...")
set_tile(center_x - 1, 45, WALL)
set_tile(center_x, 45, WALL)
set_tile(center_x + 1, 45, WALL)
set_tile(center_x - 1, 21, WALL)
set_tile(center_x, 21, WALL)
set_tile(center_x + 1, 21, WALL)

# 7. 东西六宫小路
print("  铺设六宫小路...")
for r in range(15, 40):
    set_tile(15, r, FLOOR_2, GRAY_STONE)
for r in range(15, 40):
    set_tile(30, r, FLOOR_2, GRAY_STONE)

# 保存
output_path = os.path.join(base_dir, 'data/layout.json')
layout['tiles'] = tiles
layout['tileColors'] = tileColors
with open(output_path, 'w') as f:
    json.dump(layout, f, indent=2)

print(f"\n✅ 紫禁城布局优化 v3 完成！")
print(f"   输出：{output_path}")
print(f"   尺寸：{cols} x {rows} = {len(tiles)} tiles")
print(f"   tileColors: {len([c for c in tileColors if c is not None])} 个颜色配置")

# 统计
from collections import Counter
counts = Counter(tiles)
tile_names = {
    0: 'WALL', 1: 'FLOOR_1', 2: 'FLOOR_2', 3: 'FLOOR_3(草)',
    4: 'FLOOR_4', 5: 'FLOOR_5(水)', 6: 'FLOOR_6', 7: 'FLOOR_7', 8: 'VOID'
}
print(f"\n   Tile 分布:")
for tile_type, count in sorted(counts.items()):
    name = tile_names.get(tile_type, str(tile_type))
    print(f"     {name}: {count} ({count/len(tiles)*100:.1f}%)")
