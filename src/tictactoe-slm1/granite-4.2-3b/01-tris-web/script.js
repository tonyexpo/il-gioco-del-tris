// Tris Game - Human X vs Computer O
let board = {
    cells: [],
    emptyCells: []
};

let currentPlayer = 'x'; // human plays first as X
let computerMoves = false;
let gameOver = false;
let winConditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],   // rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],   // columns
    [0, 4, 8], [2, 4, 6]               // diagonals
];

// Initialize the board
function initBoard() {
    board.cells = Array(9).fill('');
    board.emptyCells = Array(9).map((_, i) => ({ row: i / 3, col: i % 3 }));
    
    // Clear previous game state
    document.querySelectorAll('.block').forEach(b => {
        b.classList.remove('x', 'o');
        b.innerHTML = '';
    });
    
    document.getElementById('playerTurn').textContent = 'HUMAN (X)';
    document.getElementById('compStatus').textContent = 'Computer playing...';
    gameOver = false;
    currentPlayer = 'x';
}

// Update board display and block content based on cell state
function updateBoard() {
    board.cells.forEach((cellValue, index) => {
        const row = Math.floor(index / 3);
        const col = index % 3;
        const block = document.querySelector(`.block[data-row="${row}" data-col="${col}"]`);
        
        if (cellValue === 'x') {
            block.classList.add('x');
            block.textContent = ''; // show Minecraft block style via CSS
        } else if (cellValue === 'o') {
            block.classList.add('o');
            block.textContent = ''; // shows as filled block
        } else {
            block.classList.remove('x', 'o');
            block.textContent = ''; // empty state shown via CSS color
        }
    });
}

// Check if current player has won
function checkWin() {
    for (const condition of winConditions) {
        const [r1, c1, c2] = condition;
        const val1 = board.cells[r1];
        const val2 = board.cells[c1];
        const val3 = board.cells[c2];
        
        if (val1 === val2 && val2 === val3 && val1 !== '') {
            return true;
        }
    }
    return false;
}

// Check for draw (full board)
function checkDraw() {
    return board.cells.every(cell => cell !== '');
}

// Main game loop function
function makeMove(row, col) {
    if (gameOver || computerMoves && !checkWin()) {
        return false;
    }
    
    const index = row * 3 + col;
    const currentCellValue = board.cells[index];
    
    // Validate move
    if (currentCellValue !== '' || checkWin()) {
        return false;
    }
    
    // Make the move
    board.cells[index] = currentPlayer;
    board.emptyCells = board.emptyCells.filter(cell => cell !== { row: row, col: col });
    
    // Update UI
    updateBoard();
    
    // Check win or draw
    if (checkWin()) {
        gameOver = true;
        document.getElementById('playerTurn').textContent = 'GAME OVER';
        document.getElementById('compStatus').textContent = `You won!`;
        return true;
    }
    
    if (checkDraw()) {
        gameOver = true;
        document.getElementById('playerTurn').textContent = 'GAME OVER';
        document.getElementById('compStatus').textContent = 'Draw!';
        return true;
    }
    
    // Switch player
    currentPlayer = (currentPlayer === 'x') ? 'o' : 'x';
    
    // If computer's turn, make a random move or optimal AI response
    if (!computerMoves && currentPlayer === 'o') {
        // Simple AI: choose first available empty cell
        const emptyIndex = board.emptyCells[0];
        makeMove(Math.floor(emptyIndex / 3), Math.mod(emptyIndex, 3));
        return true;
    }
    
    // Human turn feedback
    document.getElementById('playerTurn').textContent = 
        (currentPlayer === 'x') ? 'COMPUTER (O)' : 'HUMAN (X)';
    
    return false;
}

// Reset the entire game
function resetGame() {
    initBoard();
    currentPlayer = 'x';
    gameOver = false;
    document.getElementById('playerTurn').textContent = 'HUMAN (X)';
    document.getElementById('compStatus').textContent = 'Computer playing...';
    
    // Clear any pending computer moves
    computerMoves = false;
}

// Event handlers
document.getElementById('resetBtn').addEventListener('click', resetGame);

document.querySelectorAll('.block').forEach(block => {
    block.addEventListener('click', (e) => {
        const row = parseInt(e.target.getAttribute('data-row'));
        const col = parseInt(e.target.getAttribute('data-col'));
        makeMove(row, col);
    });
});

// Initialize on page load
initBoard();
