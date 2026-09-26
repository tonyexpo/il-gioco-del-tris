// Tic Tac Toe Game - Human (X) vs PC (O)

const boardElement = document.getElementById('board');
const statusElement = document.getElementById('status');
const resetBtn = document.getElementById('reset-btn');
const cells = document.querySelectorAll('.cell');

let gameState = ['', '', '', '', '', '', '', '', ''];
let gameActive = true;
const HUMAN_PLAYER = 'X';
const PC_PLAYER = 'O';

// Winning combinations (indices)
const winningCombinations = [
    [0, 1, 2], // Top row
    [3, 4, 5], // Middle row
    [6, 7, 8], // Bottom row
    [0, 3, 6], // Left column
    [1, 4, 7], // Middle column
    [2, 5, 8], // Right column
    [0, 4, 8], // Diagonal top-left to bottom-right
    [2, 4, 6]  // Diagonal top-right to bottom-left
];

// Initialize game
function initGame() {
    gameState = ['', '', '', '', '', '', '', '', ''];
    gameActive = true;
    statusElement.textContent = `Player ${HUMAN_PLAYER}'s turn`;
    cells.forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('x', 'o', 'taken', 'winning');
    });
}

// Handle cell click
function handleCellClick(clickedCellEvent) {
    const clickedCell = clickedCellEvent.target;
    const clickedCellIndex = parseInt(clickedCell.getAttribute('data-index'));
    
    // Check if cell is already taken or game is not active
    if (gameState[clickedCellIndex] !== '' || !gameActive) {
        return;
    }
    
    // Human player move
    makeMove(clickedCellIndex, HUMAN_PLAYER);
    
    // Check for win/draw after human move
    if (checkWin(gameState)) {
        endGame(false);
        return;
    } else if (checkDraw(gameState)) {
        endGame(true);
        return;
    }
    
    // PC player's turn
    gameActive = false;
    statusElement.textContent = `PC is thinking...`;
    
    // Small delay for realism
    setTimeout(() => {
        const bestMoveIndex = getBestMove();
        makeMove(bestMoveIndex, PC_PLAYER);
        
        if (checkWin(gameState)) {
            endGame(false);
        } else if (checkDraw(gameState)) {
            endGame(true);
        } else {
            gameActive = true;
            statusElement.textContent = `Player ${HUMAN_PLAYER}'s turn`;
        }
    }, 500);
}

// Make a move on the board
function makeMove(index, player) {
    gameState[index] = player;
    const cell = cells[index];
    cell.textContent = player;
    cell.classList.add(player.toLowerCase(), 'taken');
}

// Check for win condition
function checkWin(boardState) {
    return winningCombinations.some(combination => {
        return combination.every(index => {
            return boardState[index] === HUMAN_PLAYER || boardState[index] === PC_PLAYER;
        });
    });
}

// Get winning cells and highlight them
function getWinningCells(boardState) {
    for (let i = 0; i < winningCombinations.length; i++) {
        const combination = winningCombinations[i];
        if (combination.every(index => boardState[index] === HUMAN_PLAYER || boardState[index] === PC_PLAYER)) {
            return combination;
        }
    }
    return null;
}

// Check for draw condition
function checkDraw(boardState) {
    return boardState.every(cell => cell !== '');
}

// End the game
function endGame(draw) {
    gameActive = false;
    if (draw) {
        statusElement.textContent = "It's a draw!";
    } else {
        const winningCells = getWinningCells(gameState);
        if (winningCells) {
            winningCells.forEach(index => {
                cells[index].classList.add('winning');
            });
            statusElement.textContent = `Player ${HUMAN_PLAYER} wins!`;
        } else {
            // This shouldn't happen but just in case
            statusElement.textContent = "Game ended unexpectedly";
        }
    }
}

// Simple AI - PC player strategy
function getBestMove() {
    let moveIndex;
    
    // Strategy 1: Try to win if possible
    moveIndex = findWinningMove(PC_PLAYER);
    if (moveIndex !== null) {
        return moveIndex;
    }
    
    // Strategy 2: Block human from winning
    moveIndex = findWinningMove(HUMAN_PLAYER);
    if (moveIndex !== null) {
        return moveIndex;
    }
    
    // Strategy 3: Take center if available
    if (gameState[4] === '') {
        return 4;
    }
    
    // Strategy 4: Take a random corner
    const corners = [0, 2, 6, 8];
    moveIndex = corners.find(index => gameState[index] === '');
    if (moveIndex !== undefined) {
        return moveIndex;
    }
    
    // Strategy 5: Take any available side
    const sides = [1, 3, 5, 7];
    moveIndex = sides.find(index => gameState[index] === '');
    if (moveIndex !== undefined) {
        return moveIndex;
    }
    
    // Fallback: First available spot
    for (let i = 0; i < 9; i++) {
        if (gameState[i] === '') {
            return i;
        }
    }
    
    return null;
}

// Find a move that would complete a winning line for a given player
function findWinningMove(player) {
    for (let i = 0; i < winningCombinations.length; i++) {
        const combination = winningCombinations[i];
        const cellsInCombination = combination.map(index => gameState[index]);
        
        // Count how many cells are already the player's mark
        const playerCount = cellsInCombination.filter(cell => cell === player).length;
        const emptyCount = cellsInCombination.filter(cell => cell === '').length;
        
        if (playerCount === 2 && emptyCount === 1) {
            // Find which cell is empty and return its index
            for (let j = 0; j < combination.length; j++) {
                if (gameState[combination[j]] === '') {
                    return combination[j];
                }
            }
        }
    }
    return null;
}

// Event listeners
cells.forEach(cell => {
    cell.addEventListener('click', handleCellClick);
});

resetBtn.addEventListener('click', initGame);

// Start the game
initGame();