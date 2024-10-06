# Chess-AI

## Overview

This project implements a Chess AI capable of playing against human opponents or other bots. The AI incorporates advanced algorithms to analyze and compute optimal moves, simulating the playing style of a grandmaster. It offers customizable themes, move translation, and a smooth visual experience using the drag-and-drop method for pieces.

## Project Structure

assets/: This directory contains all the necessary media, such as images, sounds, and themes, used during gameplay.
gameplay.gif: A visual demonstration showcasing a chess game with the AI in action.
LICENSE: License information governing the use and distribution of this project.
requirements.txt: A list of Python dependencies required to run the project. Ensure that these packages are installed before running the chess AI.
src/: The core of the chess engine and game. It includes the following critical modules:
src/agents.py: Handles different types of agents, including AI and human players.
src/board.py: Manages the chessboard and its state. This includes tracking the positions of all pieces, possible moves, and game status.
src/bot_player.py: Implements the AI bot logic, including move selection and game strategy.
src/game.py: Contains the primary game logic, including turn management, game status, and win/loss conditions.
src/piece.py: Defines the chess pieces and their respective movement patterns according to chess rules.
src/move.py: Validates and processes chess moves, ensuring they follow the rules and logic of the game.
src/theme.py: Customizes the game's appearance, allowing players to change visual themes and board styles.

## Main Features

Human vs AI: Play against the AI bot, which simulates various levels of chess expertise.
Bot vs Bot: Observe two AI agents competing against each other, demonstrating different strategies and styles.
Piece Dragging: Supports drag-and-drop functionality to move pieces on the board visually.
Move Validation: Ensures all moves are legal, adhering to standard chess rules.
Custom Themes: Switch between different board styles and themes to personalize the gaming experience.
