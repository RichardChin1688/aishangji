// 紫禁城风格布局生成器
// 生成中轴线对称、带金水河、御花园、草地、假山的布局

const COLS = 80;
const ROWS = 45;

// 地形类型
const TILE = {
  GRASS: 0,      // 草地
  FLOOR: 1,      // 宫殿地板/石板路
  WALL: 2,       // 墙壁/柱子
  WATER: 3,      // 金水河（水）
  BRIDGE: 4,     // 汉白玉桥
  ROCK: 5,       // 假山/石头
  TREE: 6,       // 古树
  PAVILION: 7,   // 亭子
  FURNITURE: 8,  // 家具（桌椅屏风）
  PATH: 9,       // 小路
};

// 初始化全草地
let tiles = new Array(ROWS * COLS).fill(TILE.GRASS);

function idx(col, row) {
  return row * COLS + col;
}

function set(col, row, tile) {
  if (col >= 0 && col < COLS && row >= 0 && row < ROWS) {
    tiles[idx(col, row)] = tile;
  }
}

function setRect(col1, row1, col2, row2, tile) {
  for (let r = row1; r <= row2; r++) {
    for (let c = col1; c <= col2; c++) {
      set(c, r, tile);
    }
  }
}

// 绘制墙壁（宫殿轮廓）
function drawPalace(col, row, width, height) {
  const left = Math.floor(col - width / 2);
  const right = left + width - 1;
  const top = row;
  const bottom = row + height - 1;
  
  // 四面墙
  for (let c = left; c <= right; c++) {
    set(c, top, TILE.WALL);
    set(c, bottom, TILE.WALL);
  }
  for (let r = top; r <= bottom; r++) {
    set(left, r, TILE.WALL);
    set(right, r, TILE.WALL);
  }
  
  // 内部地板
  setRect(left + 1, top + 1, right - 1, bottom - 1, TILE.FLOOR);
  
  return { left, right, top, bottom };
}

// 绘制金水河（弓形，从东向西流过太和殿前）
function drawGoldenWater() {
  // 金水河在太和殿前方（约 row 32-36）
  const centerRow = 34;
  const arcHeight = 4;
  const halfWidth = 25;
  const centerX = COLS / 2;
  
  for (let x = 0; x < COLS; x++) {
    const distFromCenter = Math.abs(x - centerX);
    if (distFromCenter <= halfWidth) {
      // 弓形曲线：中间高（北），两边低（南）
      const arcOffset = Math.floor(arcHeight * (1 - (distFromCenter / halfWidth) ** 2));
      const riverRow = centerRow - arcOffset;
      
      // 河流宽度 2-3 格
      set(x, riverRow, TILE.WATER);
      set(x, riverRow + 1, TILE.WATER);
      
      // 河岸
      if (riverRow > 0) set(x, riverRow - 1, TILE.GRASS);
      set(x, riverRow + 2, TILE.GRASS);
    }
  }
  
  // 金水桥（5 座汉白玉桥，横跨金水河）
  const bridgePositions = [
    Math.floor(centerX) - 20,
    Math.floor(centerX) - 10,
    Math.floor(centerX),
    Math.floor(centerX) + 10,
    Math.floor(centerX) + 20,
  ];
  
  bridgePositions.forEach(bridgeX => {
    const distFromCenter = Math.abs(bridgeX - centerX);
    const arcOffset = Math.floor(arcHeight * (1 - (distFromCenter / halfWidth) ** 2));
    const riverRow = centerRow - arcOffset;
    
    // 桥宽 3 格
    set(bridgeX - 1, riverRow, TILE.BRIDGE);
    set(bridgeX, riverRow, TILE.BRIDGE);
    set(bridgeX + 1, riverRow, TILE.BRIDGE);
    set(bridgeX - 1, riverRow + 1, TILE.BRIDGE);
    set(bridgeX, riverRow + 1, TILE.BRIDGE);
    set(bridgeX + 1, riverRow + 1, TILE.BRIDGE);
  });
}

// 绘制御花园（最北端，row 0-12）
function drawImperialGarden() {
  // 御花园区域：row 0-12, col 20-60
  
  // 堆秀山（御花园中心假山）
  const hillCenterX = 40;
  const hillCenterY = 6;
  for (let r = 0; r <= 3; r++) {
    const width = 8 - r * 2;
    setRect(hillCenterX - width, hillCenterY - r, hillCenterX + width, hillCenterY - r, TILE.ROCK);
  }
  
  // 古树（御花园四周）
  const treePositions = [
    [25, 4], [30, 3], [50, 3], [55, 4],
    [23, 8], [57, 8],
    [25, 11], [35, 10], [45, 10], [55, 11],
  ];
  treePositions.forEach(([tx, ty]) => set(tx, ty, TILE.TREE));
  
  // 亭子（东西各一个）
  setRect(28, 5, 32, 7, TILE.PAVILION);
  setRect(48, 5, 52, 7, TILE.PAVILION);
  
  // 御花园小路
  for (let c = 20; c <= 60; c++) {
    set(c, 10, TILE.PATH);
  }
  for (let r = 0; r <= 12; r++) {
    set(40, r, TILE.PATH);
  }
}

// 绘制东西六宫草地
function drawConsortsCourtyards() {
  // 东六宫草地（右侧）
  setRect(50, 15, 75, 35, TILE.GRASS);
  
  // 西六宫草地（左侧）
  setRect(5, 15, 30, 35, TILE.GRASS);
  
  // 草地小路
  for (let r = 15; r <= 35; r++) {
    set(15, r, TILE.PATH);  // 西六宫中轴
    set(65, r, TILE.PATH);  // 东六宫中轴
  }
}

// 绘制主要宫殿
function drawMainPalaces() {
  // 太和殿（最大，row 36-42）
  drawPalace(40, 36, 24, 7);
  
  // 中和殿（太和殿后，row 30-33）
  drawPalace(40, 30, 12, 4);
  
  // 保和殿（中和殿后，row 24-28）
  drawPalace(40, 24, 18, 5);
  
  // 乾清宫（row 18-22）
  drawPalace(40, 18, 20, 5);
  
  // 交泰殿（乾清宫后，row 14-16）
  drawPalace(40, 14, 10, 3);
  
  // 坤宁宫（row 8-12）
  drawPalace(40, 8, 18, 5);
  
  // 午门（最南端，row 42-45）
  drawPalace(40, 42, 28, 4);
}

// 添加家具（宫殿内部）
function addFurniture() {
  // 太和殿宝座（中心位置）
  set(39, 38, TILE.FURNITURE);
  set(40, 38, TILE.FURNITURE);
  set(41, 38, TILE.FURNITURE);
  
  // 乾清宫宝座
  set(39, 20, TILE.FURNITURE);
  set(40, 20, TILE.FURNITURE);
  set(41, 20, TILE.FURNITURE);
  
  // 屏风（宝座后）
  set(39, 37, TILE.WALL);
  set(40, 37, TILE.WALL);
  set(41, 37, TILE.WALL);
}

// 生成石板路（中轴线）
function drawCentralAxis() {
  // 中轴线石板路：午门→太和殿→乾清宫→御花园
  for (let r = 12; r <= 45; r++) {
    set(39, r, TILE.FLOOR);
    set(40, r, TILE.FLOOR);
    set(41, r, TILE.FLOOR);
  }
}

// 执行绘制
drawMainPalaces();
drawGoldenWater();
drawImperialGarden();
drawConsortsCourtyards();
drawCentralAxis();
addFurniture();

// 输出 JSON
const layout = {
  version: 1,
  cols: COLS,
  rows: ROWS,
  tiles: tiles,
};

import fs from 'fs';
import { fileURLToPath } from 'url';
const outputPath = process.argv[2] || 'data/layout.json';
fs.writeFileSync(outputPath, JSON.stringify(layout, null, 2));
console.log('✅ 紫禁城布局已保存至:', outputPath);
console.log('   尺寸:', COLS, 'x', ROWS);
console.log('   文件:', Math.round(fs.statSync(outputPath).size / 1024) + 'KB');
