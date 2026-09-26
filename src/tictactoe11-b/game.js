// ===== Tic Tac Toe Game Logic =====

// Constants
const BOARD_SIZE = 3;
const EMPTY = null;
const X = 'X';
const O = 'O';

// State
let board = Array(BOARD_SIZE).fill().map(() => Array(BOARD_SIZE).fill(EMPTY));
let currentPlayer = X; // Human always goes first
let gameOver = false;
let wins = []; // Array of {type, row, col} for wins
let tie = false;
let totalWins = 0;
let totalTies = 0;
let totalLosers = 0;

// DOM references
const boardEl = document.getElementById('board');
const scoreWinsEl = document.getElementById('score-wins');
const scoreTiesEl = document.getElementById('score-ties');
const scoreLosersEl = document.getElementById('score-losers');
const resetBtn = document.getElementById('resetBtn');

// ===== Initialization =====
function init() {
  // Render board
  renderBoard();
  // Reset scores
  totalWins = 0;
  totalTies = 0;
  totalLosers = 0;
  updateScore();
  // Start game
  startGame();
}

// ===== Board Rendering =====
function renderBoard() {
  boardEl.innerHTML = '';
  for (let row = 0; row < BOARD_SIZE; row++) {
    for (let col = 0; col < BOARD_SIZE; col++) {
      const cell = document.createElement('div');
      cell.className = 'cell';
      cell.dataset.row = row;
      cell.dataset.col = col;
      cell.innerHTML = `
        <div class="cell-tile" data-player="${board[row][col] || 'X'}">${board[row][col] || 'X'}</div>
      `;
      boardEl.appendChild(cell);
    }
  }
}

// ===== Game Logic =====
function startGame() {
  board = Array(BOARD_SIZE).fill().map(() => Array(BOARD_SIZE).fill(EMPTY));
  currentPlayer = X;
  gameOver = false;
  tie = false;
  wins = [];
  updateBoard();
}

function updateBoard() {
  renderBoard();
  updateScore();
}

function placeMark(row, col, player) {
  if (gameOver || row < 0 || row >= BOARD_SIZE || col < 0 || col >= BOARD_SIZE) return false;
  if (board[row][col] !== EMPTY) return false;

  board[row][col] = player;
  // Check win
  const win = checkWin(row, col, player);
  if (win) {
    gameOver = true;
    tie = false;
    // Count wins by winner
    if (win.player === X) {
      totalWins += 1;
    } else if (win.player === O) {
      totalLosers += 1;
    }
    wins.push(win);
    updateScore();
    return true;
  }

  // Check draw
  if (checkDraw()) {
    gameOver = true;
    tie = true;
    updateScore();
    return true;
  }

  // Switch player
  currentPlayer = (currentPlayer === X) ? O : X;
  return true;
}

// Win detection: returns {type, row, col, player} or null
function checkWin(row, col, player) {
  const directions = [
    [0, 1], // row
    [1, 0], // column
    [1, 1], // diagonal down-right
    [1, -1], // diagonal down-left
  ];

  for (const [dr, dc] of directions) {
    const line = [];
    let r = row, c = col;
    // Go in the direction of the move
    line.push(board[r][c]);
    for (let i = 1; i < BOARD_SIZE; i++) {
      r += dr;
      c += dc;
      if (r < 0 || r >= BOARD_SIZE || c < 0 || c >= BOARD_SIZE) break;
      line.push(board[r][c]);
    }
    // Go back in the opposite direction
    for (let i = line.length - 1; i >= 0; i--) {
      r -= dr;
      c -= dc;
      if (r < 0 || r >= BOARD_SIZE || c < 0 || c >= BOARD_SIZE) break;
      line.unshift(line[i]);
    }
    if (line.every(cell => cell === player)) {
      return { type: 'win', row, col, player };
    }
  }
  return null;
}

function checkDraw() {
  for (let r = 0; r < BOARD_SIZE; r++) {
    for (let c = 0; c < BOARD_SIZE; c++) {
      if (board[r][c] === EMPTY) return false;
    }
  }
  return true;
}

// ===== Score Updating =====
function updateScore() {
  scoreWinsEl.textContent = totalWins;
  scoreTiesEl.textContent = totalTies;
  scoreLosersEl.textContent = totalLosers;
}

// ===== Event Handling =====
function handleCellClick(row, col) {
  if (gameOver) return;

  const player = (currentPlayer === X) ? X : O;
  const result = placeMark(row, col, player);

  if (result) {
    // If game ended, show feedback
    if (gameOver) {
      // Determine winner for feedback
      const winner = wins[wins.length - 1];
      if (winner) {
        const winnerPlayer = winner.player;
        const isWin = winner.type === 'win';
        const isDraw = tie;
        const isTie = tie && !isWin;
        showFeedback(isWin, isDraw, isTie, row, col);
      }
    }
  }
}

function showFeedback(isWin, isDraw, isTie, row, col) {
  // Update tile visual feedback (optional)
  const tile = document.querySelector(`.cell-tile[data-row="${row}"][data-col="${col}"]`);
  if (tile) {
    tile.classList.add('win');
    tile.classList.remove('pop-in');
    // Re-trigger animation
    requestAnimationFrame(() => {
      tile.classList.remove('win');
      tile.classList.add('pop-in');
    });
  }
}

function showWinFeedback() {
  const winner = wins[wins.length - 1];
  if (!winner) return;
  const player = winner.player;
  const isX = player === X;
  const isDraw = false;
  const isTie = false;

  // Update score label styling
  document.querySelectorAll('.score-item').forEach(item => {
    const label = item.querySelector('.score-label');
    const value = item.querySelector('.score-value');
    if (label) {
      label.classList.remove('x-win', 'o-win');
      if (isX) label.classList.add('x-win');
      else if (isO) label.classList.add('o-win');
    }
  });
}

// ===== Reset =====
resetBtn.addEventListener('click', () => {
  if (gameOver) {
    // Re-start from a new game
    startGame();
  } else {
    startGame();
  }
});

// ===== Start =====
init();
