// Test script for Tic Tac Toe Game Logic
const gameState = ['', '', '', '', '', '', '', '', ''];
const HUMAN_PLAYER = 'X';
const PC_PLAYER = 'O';

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

function checkWin(boardState) {
    return winningCombinations.some(combination => {
        return combination.every(index => {
            return boardState[index] === HUMAN_PLAYER || boardState[index] === PC_PLAYER;
        });
    });
}

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

// Test cases
console.log('=== Tic Tac Toe Game Logic Tests ===\n');

// Test 1: Empty board - should return center (4)
gameState = ['', '', '', '', '', '', '', '', ''];
const move1 = getBestMove();
console.log(`Test 1 - Empty board: Expected 4, Got ${move1} - ${move1 === 4 ? 'PASS' : 'FAIL'}`);

// Test 2: Human has two in a row (horizontal) - PC should block
gameState = ['', 'X', '', '', '', '', '', '', ''];
const move2 = getBestMove();
console.log(`Test 2 - Block horizontal X: Expected 1, Got ${move2} - ${move2 === 1 ? 'PASS' : 'FAIL'}`);

// Test 3: PC has two in a row (vertical) - PC should win
gameState = ['', '', '', 'O', '', '', 'O', '', ''];
const move3 = getBestMove();
console.log(`Test 3 - Win vertical O: Expected 4, Got ${move3} - ${move3 === 4 ? 'PASS' : 'FAIL'}`);

// Test 4: Human has two in a row (diagonal) - PC should block
gameState = ['', '', 'X', '', 'O', '', 'X', '', ''];
const move4 = getBestMove();
console.log(`Test 4 - Block diagonal X: Expected 0, Got ${move4} - ${move4 === 0 ? 'PASS' : 'FAIL'}`);

// Test 5: Check win detection for human
gameState = ['X', '', 'X', 'O', 'O', 'O', '', '', ''];
const win5 = checkWin(gameState);
console.log(`Test 5 - Detect horizontal O win: Expected true, Got ${win5} - ${win5 ? 'PASS' : 'FAIL'}`);

// Test 6: Check draw detection
gameState = ['X', 'O', '', 'X', 'O', 'X', 'O', '', ''];
const isDraw6 = gameState.every(cell => cell !== '');
console.log(`Test 6 - Detect full board (draw): Expected true, Got ${isDraw6} - ${isDraw6 ? 'PASS' : 'FAIL'}`);

// Test 7: PC takes corner when center taken
gameState = ['', '', '', 'O', '', '', '', '', ''];
const move7 = getBestMove();
console.log(`Test 7 - Take corner when center taken: Expected 0, Got ${move7} - ${move7 === 0 ? 'PASS' : 'FAIL'}`);

// Test 8: PC blocks diagonal win attempt
gameState = ['', '', 'X', 'O', 'X', '', 'X', '', ''];
const move8 = getBestMove();
console.log(`Test 8 - Block diagonal X (2,4,6): Expected 0, Got ${move8} - ${move8 === 0 ? 'PASS' : 'FAIL'}`);

// Test 9: PC wins with diagonal
gameState = ['', '', 'O', 'X', 'O', '', 'X', '', ''];
const move9 = getBestMove();
console.log(`Test 9 - Win diagonal O (2,4,6): Expected 0, Got ${move9} - ${move9 === 0 ? 'PASS' : 'FAIL'}`);

// Test 10: PC blocks column win
gameState = ['', '', '', 'X', 'O', '', 'X', '', ''];
const move10 = getBestMove();
console.log(`Test 10 - Block vertical X (0,3,6): Expected 0, Got ${move10} - ${move10 === 0 ? 'PASS' : 'FAIL'}`);

console.log('\n=== All tests completed ===');