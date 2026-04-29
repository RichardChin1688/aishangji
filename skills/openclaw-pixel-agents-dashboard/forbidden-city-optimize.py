#!/usr/bin/env python3
# 紫禁城布局优化脚本
# 在原有布局基础上添加：金水河、御花园、草地、假山、古树、亭台等

import json
import math

# 读取原布局
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_dir, 'data/layout.json'), 'r') as f:
    layout = json.load(f)

cols = layout['cols']  # 45
rows = layout['rows']  # 80
tiles = layout['tiles']

# Tile 类型定义
TILE = {
    'FLOOR': 1,      # 地板/石板路
    'WALL': 2,       # 墙壁/柱子
    'GRASS': 3,      # 草地
    'WATER': 4,      # 水（金水河）
    'BRIDGE': 5,     # 汉白玉桥
    'ROCK': 6,       # 假山/石头
    'TREE': 7,       # 古树
    'PAVILION': 8,   # 亭子
    'PATH': 9,       # 小路
    'FURNITURE': 10, # 家具（宝座、屏风）
}

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

# 1. 铺设草地（东西六宫区域）
print("铺设草地...")
# 西六宫草地（左侧）
set_rect(5, 15, 25, 40, TILE['GRASS'])
# 东六宫草地（右侧）
set_rect(20, 15, 40, 40, TILE['GRASS'])

# 2. 绘制内金水河（太和殿前，弓形）
print("绘制金水河...")
center_x = cols // 2  # 22
river_row_base = 48  # 太和殿前方
arc_height = 3

for x in range(cols):
    dist = abs(x - center_x)
    if dist <= 18:
        # 弓形曲线
        arc_offset = int(arc_height * (1 - (dist / 18) ** 2))
        river_row = river_row_base - arc_offset
        
        # 河流（宽 2 格）
        set_tile(x, river_row, TILE['WATER'])
        set_tile(x, river_row + 1, TILE['WATER'])
        
        # 河岸草地
        if river_row > 0:
            set_tile(x, river_row - 1, TILE['GRASS'])
        set_tile(x, river_row + 2, TILE['GRASS'])

# 3. 金水桥（5 座汉白玉桥）
print("建造金水桥...")
bridge_positions = [center_x - 12, center_x - 6, center_x, center_x + 6, center_x + 12]

for bx in bridge_positions:
    dist = abs(bx - center_x)
    arc_offset = int(arc_height * (1 - (dist / 18) ** 2))
    river_row = river_row_base - arc_offset
    
    # 桥（宽 3 格）
    for dx in [-1, 0, 1]:
        set_tile(bx + dx, river_row, TILE['BRIDGE'])
        set_tile(bx + dx, river_row + 1, TILE['BRIDGE'])

# 4. 御花园（最北端，row 0-12）
print("建造御花园...")
# 堆秀山（中心假山）
hill_x, hill_y = center_x, 6
for r in range(4):
    width = 4 - r
    set_rect(hill_x - width, hill_y - r, hill_x + width, hill_y - r, TILE['ROCK'])

# 古树（御花园四周）
tree_positions = [
    (10, 4), (15, 3), (30, 3), (35, 4),
    (8, 8), (37, 8),
    (10, 11), (18, 10), (27, 10), (35, 11),
]
for tx, ty in tree_positions:
    set_tile(tx, ty, TILE['TREE'])

# 亭子（东西各一个）
set_rect(13, 5, 16, 7, TILE['PAVILION'])
set_rect(29, 5, 32, 7, TILE['PAVILION'])

# 御花园小路
for c in range(10, 36):
    set_tile(c, 9, TILE['PATH'])
for r in range(0, 13):
    set_tile(center_x, r, TILE['PATH'])

# 5. 中轴线石板路（午门→太和殿→乾清宫→御花园）
print("铺设中轴线石板路...")
for r in range(13, 60):
    set_tile(center_x - 1, r, TILE['FLOOR'])
    set_tile(center_x, r, TILE['FLOOR'])
    set_tile(center_x + 1, r, TILE['FLOOR'])

# 6. 宫殿内部装饰（宝座、屏风）
print("添加宫殿装饰...")
# 太和殿宝座（约 row 44-46）
set_tile(center_x - 1, 45, TILE['FURNITURE'])
set_tile(center_x, 45, TILE['FURNITURE'])
set_tile(center_x + 1, 45, TILE['FURNITURE'])
# 屏风
set_tile(center_x - 1, 44, TILE['WALL'])
set_tile(center_x, 44, TILE['WALL'])
set_tile(center_x + 1, 44, TILE['WALL'])

# 乾清宫宝座（约 row 20-22）
set_tile(center_x - 1, 21, TILE['FURNITURE'])
set_tile(center_x, 21, TILE['FURNITURE'])
set_tile(center_x + 1, 21, TILE['FURNITURE'])

# 7. 东西六宫小路
print("铺设六宫小路...")
# 西六宫中轴路
for r in range(15, 40):
    set_tile(15, r, TILE['PATH'])
# 东六宫中轴路
for r in range(15, 40):
    set_tile(30, r, TILE['PATH'])

# 保存新布局
output_path = os.path.join(base_dir, 'data/layout.json')
with open(output_path, 'w') as f:
    json.dump(layout, f, indent=2)

print(f"\n✅ 紫禁城布局优化完成！")
print(f"   输出：{output_path}")
print(f"   尺寸：{cols} x {rows} = {len(tiles)} tiles")
print(f"   Tile 类型：{sorted(set(tiles))}")

# 统计各 tile 数量
from collections import Counter
counts = Counter(tiles)
print(f"\n   Tile 分布:")
for tile_type, count in sorted(counts.items()):
    print(f"     {tile_type}: {count} ({count/len(tiles)*100:.1f}%)")
