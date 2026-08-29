# SEGFAULT-GameMechanics--TESTING-
A simple puzzle like game designed to run entirely on the console (Game mechanics in testing phase)

## SEGFAULT - Game Mechanics Engine (Testing Build)

A lightweight, data-driven 2D room grid engine built in modular Python. This repository serves as the architecture prototype testing spatial navigation, room matrix rendering, interactable objects, and state-driven spatial lock validation.

## 🏗️ Project Architecture & Pipeline

The project uses a strict, bottom-up decoupled dependency hierarchy. Data definitions are completely isolated from execution logic, keeping the engine micro-light (~21 KB) and free of nested conditional logic.

### Module Breakdown

| Module | Purpose |
| :--- | :--- |
| **`assets.py`** | **Pure Data Layer.** Contains static ANSI tile mappings (`TILES`), master layout definitions, raw $14 \times 10$ numerical room matrices, and raw text constants. Holds zero logic code. |
| **`GameEngine.py`** | **Key Part of the Game Engine** For now it just handles clearing lines and screen stuff, only two functions |
| **`objects.py`** | **Entity Definitions.** Class blueprints for interactive entities (`Keycard`, `Terminal`, `StorageUnit`). Tracks object IDs, item locations, inventory links, and state checks. |
| **`rooms.py`** | **Spatial Room Class.** Defines the `Room` object structure, handling directional exits (`N`, `S`, `E`, `W`), object bindings, local interactables, and exit lock status flags (`is_Locked`). |
| **`world.py`** | **World Graph.** Assembles all spatial matrices and `Room` instances into a unified graph lookup dictionary (`WORLD`), mapping cardinal room links and locking criteria. |
| **`player.py`** | **State Tracker.** For all player stuff |
| **`main.py`** | **Main Dispatch Loop.** (Work In Progress. Not added yet.) |

---

## 🎮 Engine Features

* **Matrix-Based Room Rendering:** Dynamic $14 \times 10$ spatial room grids rendered cleanly in standard terminal view.
* **Graph-Based Navigation:** Seamless movement through room connections utilizing an isolated spatial lookup dictionary.
* **Data-Driven Lock Validation:** Structural exit lock checking (`is_Locked`) blocking invalid navigation paths without execution crashes.
* **Granular Tile System:** Color-coded terminal display utilizing custom tile IDs for walls, open doors, keycard-locked doors, terminals, storage units, and interactive mystery elements.

---

## NOTE

Most of the README is written by Gemini (Turns out I absolutely suck at writing README files 😅😅). The code is all written by me though, might not be the best code out there, it is my first big project after a long break from coding. Hope you like it.
