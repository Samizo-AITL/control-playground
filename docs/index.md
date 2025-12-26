---
layout: default
title: Control Playground
---

# Control Playground

固定PID制御器が、  
**色付き（低周波）かつ状態依存の外乱**にさらされたとき、  
**時間応答だけ**を用いて挙動を観測するためのページです。

- スライダーなし  
- 位置アニメなし  
- 説明過多なし  

**y(t), setpoint(t), disturbance(t)**  
それだけが表示されます。

---

## Live Demo

<iframe
  src="../index.html"
  style="width:100%; height:360px; border:none;">
</iframe>

---

## What this shows

- PID が「追従できているように見える」理由
- なぜ低周波・状態依存外乱が効くのか
- どこで位相・積分が破綻するのか

**結論はコードではなく、波形が語ります。**

---

## Controls

- `R` : Reset  
- `SPACE` : 外乱注入（観測用）

---

## Notes

This page is intentionally minimal.

If you need intuition, look elsewhere.  
If you need truth, look at the time response.

