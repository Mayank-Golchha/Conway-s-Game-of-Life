# 🧬 Conway's Game of Life – Cellular Automata Simulator

> *"Out of simplicity, complexity is born."* — John Conway

A visually rich and interactive simulation of **Conway’s Game of Life**, demonstrating how simple rules lead to complex emergent behavior. Featuring classic patterns like **Gliders**, **Blinkers**, and **Pulsars**, this simulation offers a mesmerizing look into the world of cellular automata.

---

## 🎮 Features

- 📊 Real-time simulation with smooth animation
- ✏️ Manual cell editing or random generation
- ⏸️ Pause / Resume control
- ⚙️ Adjustable simulation speed (if supported)
- 📁 Predefined patterns: Glider, Blinker, Pulsar

---

## 🌟 What Is Conway’s Game of Life?

Conway's Game of Life is a **zero-player game** played on a grid of cells. Each cell can either be **alive** or **dead**. Cells evolve across generations based on a simple set of rules.

### 🧪 The Rules:
The game evolves over time based on these four simple rules:

1. 🏜️ **Underpopulation**  
   A live cell with **fewer than 2 live neighbors** dies.

2. 🌿 **Survival**  
   A live cell with **2 or 3 live neighbors** stays alive.

3. 🔥 **Overpopulation**  
   A live cell with **more than 3 live neighbors** dies.

4. 🌱 **Reproduction**  
   A dead cell with **exactly 3 live neighbors** becomes a live cell.

---

## 🎥 Demo Patterns

### 🛩️ Glider
A tiny spaceship that moves diagonally forever.

![Game_of_life_animated_glider](https://github.com/user-attachments/assets/ade7725c-e7eb-4d88-a7e2-3d145f23cd0a)

---

### ✨ Blinker  
A simple oscillator that flips between two states.

![Game_of_life_blinker](https://github.com/user-attachments/assets/39845dc1-16f7-42fb-ade0-50322651c39a)


---

### 🌌 Pulsar  
A large symmetric oscillator with a 3-generation cycle.

![Game_of_life_pulsar](https://github.com/user-attachments/assets/ea760beb-4ee9-4efa-8180-7701dde0115c)


---

## 🎮 How to Use

- 🔲 **Step 1: Design your pattern**
  - Press **Shift** once to **enter cell selection mode**.
  - Click on the grid to **toggle cells on/off** (alive/dead).
  
- ▶️ **Step 2: Start the simulation**
  - Press **Shift** again to **begin the simulation**.
  - Watch the cells evolve over generations!

> ⏸️ You can press Shift again to stop and modify the pattern.


## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mayank-Golchha/Conway-s-Game-of-Life.git
   cd Conway-s-Game-of-Life
