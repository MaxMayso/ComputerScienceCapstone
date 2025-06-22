# Computer Science Capstone Project
This Repository is for Computer Science Capstone for SNHU's CS499 capstone course.

![language](https://img.shields.io/badge/language-Python-cyan)
![editor](https://img.shields.io/badge/editor-VSCode-lightpink)

## Project Overview

The primary artifact in this ePortfolio is a Python-based text adventure game titled **Protect and Serve**. Originally developed as a foundational exercise in procedural programming, the project was enhanced throughout the capstone course to meet professional software standards and to reflect skills gained during the Computer Science program.

---

## Enhancements List

### 1. Software Design and Engineering
The game code was refactored into a modular, object-oriented structure. The original single-file script was split into multiple organized modules (`player.py`, `mechanics.py`, `config.py`, `game.py`) to improve readability, scalability, and maintainability.
This is much more efficient rather than it's original state where the entire game was being run in the same file of code. This would mean the entire file would compile when the game was run.

### 2. Algorithms and Data Structures
The command parser was enhanced to intelligently interpret directional input and manage game flow logic more efficiently. This allows a simpler more user-friendly command array for directional input. Inventory management and item tracking were also improved to better reflect the use of core data structures like sets and dictionaries.

### 3. Databases
A JSON-based save/load system was implemented to allow players to persist game state. This enhancement demonstrates the application of structured data handling and file I/O operations to support user session continuity. This allows the player to save the game at checkpoints throughout the game and return to their progress at their own convenience.

---

## Technologies Used

- Original File - Python 3.9 | Updated file 3.10.1
- JSON (for game state serialization)
- Git/GitHub (for version control and portfolio publishing)

---

## About This Portfolio

This project is part of a professional portfolio aimed at demonstrating real-world application of computer science fundamentals. It represents my growth as a software developer and reflects my interests in DevSecOps, cloud computing, and secure software architecture. The project meets or exceeds the requirements defined in the CS 499 Capstone Project Guidelines as requested in the rubric, showcasing my preparedness for industry-level software development.

---

## Narrative 

For the database enhancement, I continued work on my original SNHU140 Python game, Protect and Serve. The focus this time was implementing a way to persist player progress between game sessions using JSON file storage. This added a real-world feature that would be expected in even basic modern applications, saving and loading data. I started with a modular, object-oriented structure from previous enhancements, which made it easier to insert new features cleanly and test them independently. I chose this artifact for enhancement in the databases category because it gave me the opportunity to demonstrate how structured data can be serialized, stored, and retrieved using JSON.a lightweight but widely used data exchange format. Rather than using something like a SQL or NoSQL database, I decided to go with a more self-contained solution that made sense for the size and purpose of the game allowing to be as great as I had imagined it. I wanted this enhancement to feel like a natural extension of the project, not just something added for the sake of checking a box. For me, it's important that each improvement reflects how much I've grown as a developer. This feature not only made the game more useful for players but also gave me a chance to apply what I’ve learned about managing data in a real, hands-on way.

To accomplish this, I added methods to the GameState class to convert the internal state of the game to and from JSON format. This included handling edge cases like missing files and ensuring the save file was named per user. The player’s inventory, current room, and overall game progress are now saved automatically without the player needing to type “save” constantly. At first I added a simple save feature that allowed the player to save after input. This was shortlived after being more comfortable with the save algorithms I then upgraded the game to provide an auto-save feature that records the game's process immediately after the user exits the game through the exit command. On game start, it checks for an existing save and reloads the last session if available.

This enhancement let me meet the goals I set in my Module One plan. I demonstrated how to integrate file handling, data persistence, and user state recovery into a Python-based program. While it wasn’t an enterprise-level database, it was an effective way to show working knowledge of data storage principles in a scoped project. It helped me further internalize how even basic programs benefit from structured data systems.

Looking back, I learned how to manage file I/O cleanly and anticipate errors like missing or corrupted save files. One challenge I faced was figuring out where the save/load logic belonged, balancing convenience for the player without making the game logic feel bloated. I resolved this by isolating save/load logic in the GameState class and using method calls in the game loop that don’t clutter user experience.

This enhancement really brought my artifact full circle. From a single file with hardcoded logic to a modular, scalable, and persistent application—this journey has shown me how far I’ve come since I first started. It also reinforced how databases and data storage principles are relevant even in the smallest of projects.

--- 



