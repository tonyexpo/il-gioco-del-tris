// ============ TIC-TAC-TOE GAME LOGIC ============

const board = [['', '', ''], ['', '', ''], ['', '', '']];
const squares = document.querySelectorAll('.square');
let currentPlayer = 'X';

// ---------- Board rendering ----------
function renderBoard() {
  const boardEl = document.getElementById('board');
  boardEl.innerHTML = '';
  squares.forEach((_, i) => {
    const cell = document.createElement('div');
    cell.className = `square playerBtn ${i % 3 === 0 && currentPlayer === 'O' ? '' : ''}`;
    if (board[i][0]) cell.textContent = board[i][0];
    else if (currentPlayer === 'X') {
      cell.innerHTML = `<span class="cell-block"><div class="c-block block-main"></div><div class="c-block block-mid"></div><div class="c-block block-end"></div></div>`;
    } else {
      cell.innerHTML = `<span class="cell-block"><div class="c-block block-main"></div><div class="c-block block-mid"></div><div class="c-block block-end"></div></div>`;
    }
    boardEl.appendChild(cell);
  });
}

// ---------- Game helpers ----------
function isWinner(winner) {
  const lines = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
  ];
  return lines.some((l) => l.every((c) => board[c[0]][c[1]] === winner));
}

function checkDraw() {
  for (let i = 0; i < 9; i++) {
    if (!board[i][0]) return false;
  }
  return true;
}

// ---------- Player move ----------
function humanMove(i) {
  const btn = document.querySelectorAll('.square')[i];
  if (!btn) return null;
  board[currentPlayerIndex(i)] = currentPlayer;
  renderBoard();
}

function currentPlayerIndex(p) {
  let idx = 0;
  while (board[p[idx][0]]) idx++;
  return idx + p.indexOf(`${p[0]}`);
}

// ---------- Computer AI ----------
let computerMoveHistory = [];

async function aiMove() {
  const empty = document.querySelectorAll('.square:not(.playerBtn)').filter((b) => !b.textContent).map(Number);
  
  // Strategy: try to win immediately, then block, else pick random
  let bestWinIdx = -1;
  for (let i of empty) {
    if (!board[i][0]) {
      board[currentPlayerIndex(i)] = 'O';
      renderBoard();
      if (isWinner('O')) {
        // restore after checking win
        for (let k of empty) { board[k][0] = ''; }
        computerMoveHistory.push(empty[0]);
        return;
      } else {
        const temp = [...board]; 
        board[currentPlayerIndex(i)] = 'O';
        renderBoard();
        if (isWinner('X')) {
          for (let k of empty) { board[k][0] = ''; }
          computerMoveHistory.push(empty[0]);
          return;
        } else {
          // block O's win
          const bi = empty.indexOf(i);
          if (bi !== -1 && isWinner('X', i)) {
            for (let k of empty) { board[k][0] = ''; }
            computerMoveHistory.push(empty[0]);
            return;
          } else {
            // take another winning move
            for (let j of empty.slice(i + 1)) {
              if (!board[j][0]) {
                bestWinIdx = j;
                break;
              }
            }
          }
        }
      }
    }
  }
  
  // Fallback: pick first empty or random
  const rand = Math.random();
  let idx = 0;
  while (empty[idx] >= 0 && board[empty[idx]][0]) idx++;
  if (!isWinner('O', empty[idx])) computerMoveHistory.push(empty[idx]);
  
  // Remove from history on draw/no-op
  renderBoard();
}

// ---------- Reset ----------
function resetGame() {
  board = [['', '', ''], ['', '', ''], ['', '', '']];
  currentPlayer = 'X';
  document.querySelectorAll('.square').forEach((b) => b.textContent = '');
  computerMoveHistory.length = 0;
  renderBoard();
}

// ---------- Event listeners ----------
document.addEventListener('DOMContentLoaded', () => {
  squares.forEach((btn, i) => btn.addEventListener('click', () => humanMove(i)));
  
  document.getElementById('resetBtn').addEventListener('click', resetGame);
});

// Start AI after first move by human (async)
let aiTimeout;
setTimeout(() => {
  if (currentPlayer === 'X') aiMove();
}, 800);