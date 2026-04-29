#!/usr/bin/env python3
# 紫禁城布局优化 v2 - 使用系统支持的 Tile 类型
# TileType: 0=WALL, 1-7=FLOOR, 8=VOID
# 策略：
#   - 草地 → FLOOR_3 (3) 绿色系
#   - 金水河 → FLOOR_5 (5) 蓝色系
#   - 汉白玉桥 → FLOOR_1 (1) 浅色
#   - 假山 → WALL (0) 堆叠
#   - 小路 → FLOOR_2 (2) 石板色
#   - 宫殿地板 → FLOOR_1 (1)

import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_dir, 'data/layout.json'), 'r') as f:
    layout = json.load(f)

cols = layout['cols']  # 45
rows = layout['rows']  # 80
tiles = layout['tiles']

# Tile 类型（系统支持的）
WALL = 0
FLOOR_1 = 1  # 浅色 - 宫殿地板、汉白玉桥
FLOOR_2 = 2  # 石板色 - 小路
FLOOR_3 = 3  # 绿色 - 草地
FLOOR_4 = 4  # 深绿 - 备用草地
FLOOR_5 = 5  # 蓝色 - 金水河
FLOOR_6 = 6  # 深蓝 - 备用
FLOOR_7 = 7  # 紫色 - 备用
VOID = 8

def idx(col, row):
    return row * cols + col

def get(col, row):
    if 0 <= col < cols and 0 <= row < rows:
        return tiles[idx(col, row)]
    return None

def set_tile(col, row, tile_type):
    if 0 <= col < cols and 0 <= row < rows:
        tiles[idx(col, row)] = tile_type

def set_rect(col1, row1, col2, row2, tile_type):
    for r in range(row1, min(row2 + 1, rows)):
        for c in range(col1, min(col2 + 1, cols)):
            tiles[idx(c, r)] = tile_type

print("开始紫禁城布局优化...")

# 1. 铺设草地（东西六宫区域）- FLOOR_3 (绿色)
print("  铺设草地...")
# 西六宫草地（左侧）
set_rect(5, 15, 25, 40, FLOOR_3)
# 东六宫草地（右侧）
set_rect(20, 15, 40, 40, FLOOR_3)

# 2. 绘制内金水河（太和殿前，弓形）- FLOOR_5 (蓝色)
print("  绘制金水河...")
center_x = cols // 2  # 22
river_row_base = 48  # 太和殿前方
arc_height = 3

for x in range(cols):
    dist = abs(x - center_x)
    if dist <= 18:
        arc_offset = int(arc_height * (1 - (dist / 18) ** 2))
        river_row = river_row_base - arc_offset
        
        # 河流（宽 2 格）
        set_tile(x, river_row, FLOOR_5)
        set_tile(x, river_row + 1, FLOOR_5)
        
        # 河岸草地
        if river_row > 0:
            set_tile(x, river_row - 1, FLOOR_3)
        set_tile(x, river_row + 2, FLOOR_3)

# 3. 金水桥（5 座汉白玉桥）- FLOOR_1 (浅色)
print("  建造金水桥...")
bridge_positions = [center_x - 12, center_x - 6, center_x, center_x + 6, center_x + 12]

for bx in bridge_positions:
    dist = abs(bx - center_x)
    arc_offset = int(arc_height * (1 - (dist / 18) ** 2))
    river_row = river_row_base - arc_offset
    
    # 桥（宽 3 格）
    for dx in [-1, 0, 1]:
        set_tile(bx + dx, river_row, FLOOR_1)
        set_tile(bx + dx, river_row + 1, FLOOR_1)

# 4. 御花园（最北端，row 0-12）
print("  建造御花园...")
# 堆秀山（中心假山）- 用 WALL 堆叠
hill_x, hill_y = center_x, 6
for r in range(4):
    width = 4 - r
    set_rect(hill_x - width, hill_y - r, hill_x + width, hill_y - r, WALL)

# 御花园草地
set_rect(10, 2, 35, 12, FLOOR_3)

# 古树位置（用 WALL 标记，后续可替换为家具）
tree_positions = [
    (10, 4), (15, 3), (30, 3), (35, 4),
    (8, 8), (37, 8),
    (10, 11), (18, 10), (27, 10), (35, 11),
]
for tx, ty in tree_positions:
    set_tile(tx, ty, WALL)

# 亭子（东西各一个）- 用 FLOOR_1 浅色
set_rect(13, 5, 16, 7, FLOOR_1)
set_rect(29, 5, 32, 7, FLOOR_1)

# 御花园小路 - FLOOR_2
for c in range(10, 36):
    set_tile(c, 9, FLOOR_2)
for r in range(0, 13):
    set_tile(center_x, r, FLOOR_2)

# 5. 中轴线石板路（午门→太和殿→乾清宫→御花园）- FLOOR_2
print("  铺设中轴线石板路...")
for r in range(13, 60):
    set_tile(center_x - 1, r, FLOOR_2)
    set_tile(center_x, r, FLOOR_2)
    set_tile(center_x + 1, r, FLOOR_2)

# 6. 宫殿内部装饰（宝座区域）- 用 WALL 标记
print("  添加宫殿装饰...")
# 太和殿宝座区域（约 row 44-46）
set_tile(center_x - 1, 45, WALL)
set_tile(center_x, 45, WALL)
set_tile(center_x + 1, 45, WALL)

# 乾清宫宝座区域（约 row 20-22）
set_tile(center_x - 1, 21, WALL)
set_tile(center_x, 21, WALL)
set_tile(center_x + 1, 21, WALL)

# 7. 东西六宫小路 - FLOOR_2
print("  铺设六宫小路...")
# 西六宫中轴路
for r in range(15, 40):
    set_tile(15, r, FLOOR_2)
# 东六宫中轴路
for r in range(15, 40):
    set_tile(30, r, FLOOR_2)

# 保存新布局
output_path = os.path.join(base_dir, 'data/layout.json')
with open(output_path, 'w') as f:
    json.dump(layout, f, indent=2)

print(f"\n✅ 紫禁城布局优化完成！")
print(f"   输出：{output_path}")
print(f"   尺寸：{cols} x {rows} = {len(tiles)} tiles")

# 统计各 tile 数量
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
