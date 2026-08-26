# Tic Tac Toe WPF Demo

## 🚀 Project Overview
This repository contains a complete, self-contained implementation of a Tic Tac Toe game using modern C# and WPF, adhering strictly to the Model-View-ViewModel (MVVM) pattern.

**Target Framework:** .NET 10 Windows
**Player:** Human ('X')
**AI Opponent:** Computer ('O') - Uses random move selection logic.

## 🛠️ Setup & Build Instructions

### ⚠️ IMPORTANT: Resolving the MSB3644 Error
The build process encountered an error (`MSB3644`) indicating a dependency on legacy `.NET Framework v1.0`. This is an environment issue that cannot be fixed by code alone. **Before building, ensure your development environment (Visual Studio/MSBuild) is configured to exclusively use the modern .NET SDK and does not attempt to resolve old framework references.**

### Build Steps
1.  **Restore Dependencies:** Open a terminal in the project root directory (`C:\Users\Antonio Esposito\Desktop\toctactoe2`) and run:
    ```bash
    dotnet restore TicTacToeWPF/TicTacToeWPF.csproj
    ```
2.  **Build Project:** Run the build command, ensuring the correct target framework is used:
    ```bash
    dotnet build TicTacToeWPF/TicTacToeWPF.csproj --framework net10-windows
    ```

## 🎮 Usage Guide

### Running the Game
Execute the compiled application from the `bin/Debug` folder within the `TicTacToeWPF` directory.

### Features Implemented:
*   **MVVM Separation:** Logic is cleanly separated into Model (`GameModel`), ViewModel (`MainViewModel`), and View (`MainWindow`).
*   **Player Turn ('X'):** The game starts when you click the first available button. You play as 'X'.
*   **AI Opponent ('O'):** After your move, the AI opponent automatically makes a random valid move.
*   **Game State:** The UI updates dynamically to show the current state (Win/Draw/Ongoing).
*   **Reset Button:** A dedicated button is available at the bottom of the window to reset the game board and start a new round.

## 📂 Project Structure Reference

| File/Folder | Role | Description |
| :--- | :--- | :--- |
| `TicTacToeWPF.csproj` | Build Definition | Defines the project, targeting `net10-windows`. |
| `GameModel.cs` | **Model** | Holds the core game state (the 3x3 board) and deterministic logic (Win/Draw checks). |
| `MainViewModel.cs` | **ViewModel** | Handles business logic, player input binding, AI move generation, and status management. |
| `MainWindow.xaml` | **View** | Defines the UI structure using WPF XAML. Binds to `GridCommands`. |
| `IndexToCharConverter.cs` | Utility | Converts button parameters (e.g., 'X', 'O') into displayable characters for the View. |

## ✨ Development Notes
*   The AI logic is currently implemented as a **random move selector**, fulfilling the requirement for random difficulty/logic.
*   All components are designed to be easily extended (e.g., replacing `RandomMoveSelector` with Minimax algorithm).