---
title: Animation Test Documentation
---

# Animation Test

このページは、`animation-test` リポジトリにおける  
**アニメーション実験・設計検証用の説明ページ**です。

---

## 🔗 Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/animation-test/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/animation-test/tree/main) |

[![Back to Samizo-AITL Portal](https://img.shields.io/badge/Back%20to%20Samizo--AITL%20Portal-brightgreen)](https://samizo-aitl.github.io) 

---

## 概要

トップページでは、以下の方針でアニメーションを実装しています。

- HTML + Canvas のみ
- 外部ライブラリ不使用
- `requestAnimationFrame` による描画同期
- 数式的に定義された運動（調和振動）

---

## 実装の要点

### 時間更新

```js
let t = 0;
t += 0.03;
```

- 実時間に依存せず、**安定した視覚検証**を優先
- デモ用途ではこの方式が最も事故らない

---

### 描画モデル

位置は以下で定義しています。

\[
x(t) = x_0 + A \sin(t)
\]

- $x_0$ : 中心位置  
- $A$ : 振幅  

---

## 用途

- モーション表現の試験
- 制御・物理モデル可視化の前段
- Canvas 描画負荷評価
- 将来の SVG / WebGL 展開のベース

---

## 方針

このリポジトリは以下を **意図的に含みません**。

- フレームワーク依存
- ビルド工程
- CSS アニメーション乱用

「**読めば分かる・直せば動く**」を最優先とします。

---

## 戻る

- [トップページへ](../)

