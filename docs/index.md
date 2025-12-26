---
layout: default
title: Control Playground
---

# Control Playground

---

## 🔗 Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/control-playground/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/control-playground/tree/main) |

---

A page to observe the behavior of a **fixed PID controller**  
when subjected to **colored (low-frequency) and state-dependent disturbances**,  
using **time responses only**.

- No sliders  
- No position animation  
- No excessive explanation  

Only these signals are shown:

**y(t), setpoint(t), disturbance(t)**

---

## Live Demo

<iframe
  src="../index.html"
  style="width:100%; height:360px; border:none;">
</iframe>

---

## What this shows

- Why the PID *appears* to be tracking correctly  
- Why low-frequency, state-dependent disturbances are effective  
- Where phase and integral action break down  

**The conclusion is not in the code — the waveforms speak for themselves.**

---

## Controls

- `R` : Reset  
- `SPACE` : Inject disturbance (for observation)

---

## Notes

This page is intentionally minimal.

If you need intuition, look elsewhere.  
If you need truth, look at the time response.

