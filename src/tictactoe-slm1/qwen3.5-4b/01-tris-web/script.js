// Tic Tac Toe - X vs PC (O)
const board = document.getElementById('board');
const cells = Array.from(document.querySelectorAll('.cell'));
const statusDisplay = document.getElementById('status');
const currentPlayerDisplay = document.getElementById('current-player');
const resetBtn = document.getElementById('reset-btn');

let gameState = ['', '', '', '', '', '', '', '', ''];
let gameActive = true;
const HUMAN = 'X';
const PC = 'O';

// Win combinations
const winConditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
    [0, 4, 8], [2, 4, 6]             // Diagonals
];

// Check if player has won
function checkWin(player) {
    return winConditions.some(condition => {
        return condition.every(index => gameState[index] === player);
    });
}

// Check for draw
function checkDraw() {
    return !gameState.includes('') && !checkWin(HUMAN) && !checkWin(PC);
}

// Update status display
function updateStatus(message, color = '#ffd700') {
    statusDisplay.textContent = message;
    statusDisplay.style.color = color;
}

// Handle cell click
function handleCellClick(index) {
    if (gameState[index] !== '' || !gameActive) return;
    
    // Human's turn
    makeMove(HUMAN, index);
    
    if (checkWin(HUMAN)) {
        gameActive = false;
        updateStatus('VITTORIA! Hai vinto!', '#4fc3f7');
        cells[index].classList.add('x');
        return;
    }
    
    if (checkDraw()) {
        gameActive = false;
        updateStatus('PAREGGIO!', '#ffd700');
        return;
    }
    
    // PC's turn with delay for realism
    setTimeout(() => {
        makeMove(PC, getBestMove());
        
        if (checkWin(PC)) {
            gameActive = false;
            updateStatus('VITTORIA PC! Hai perso!', '#f44336');
            cells[getBestMove()].classList.add('o');
            return;
        }
        
        if (checkDraw()) {
            gameActive = false;
            updateStatus('PAREGGIO!', '#ffd700');
            return;
        }
        
        // Human's turn again
        currentPlayerDisplay.textContent = HUMAN;
    }, 500);
}

// Make a move
function makeMove(player, index) {
    gameState[index] = player;
    cells[index].textContent = player === HUMAN ? 'X' : 'O';
    cells[index].classList.add(player.toLowerCase());
}

// Get best move using Minimax algorithm
function getBestMove() {
    let bestScore = -Infinity;
    let move = -1;
    
    for (let i = 0; i < 9; i++) {
        if (gameState[i] === '') {
            gameState[i] = PC;
            let score = minimax(gameState, 0, false);
            gameState[i] = '';
            
            if (score > bestScore) {
                bestScore = score;
                move = i;
            }
        }
    }
    
    return move;
}

// Minimax algorithm for optimal play
function minimax(board, depth, isMaximizing) {
    if (checkWin(PC)) return 10 - depth;
    if (checkWin(HUMAN)) return depth - 10;
    if (checkDraw()) return 0;
    
    if (isMaximizing) {
        let bestScore = -Infinity;
        for (let i = 0; i < 9; i++) {
            if (board[i] === '') {
                board[i] = PC;
                let score = minimax(board, depth + 1, false);
                board[i] = '';
                bestScore = Math.max(score, bestScore);
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < 9; i++) {
            if (board[i] === '') {
                board[i] = HUMAN;
                let score = minimax(board, depth + 1, true);
                board[i] = '';
                bestScore = Math.min(score, bestScore);
            }
        }
        return bestScore;
    }
}

// Reset game
function resetGame() {
    gameState = ['', '', '', '', '', '', '', '', ''];
    gameActive = true;
    cells.forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('x', 'o');
    });
    updateStatus('', '#ffd700');
    currentPlayerDisplay.textContent = HUMAN;
}

// Event listeners
cells.forEach((cell, index) => {
    cell.addEventListener('click', () => handleCellClick(index));
});

resetBtn.addEventListener('click', resetGame);

// Start game
currentPlayerDisplay.textContent = HUMAN;