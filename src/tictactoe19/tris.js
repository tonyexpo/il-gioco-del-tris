// Tris (Tic Tac Toe) - Giocatore X vs PC (O)
// AI: minimax semplice

class TicTacToe {
    constructor() {
        this.board = Array(9).fill(null);
        this.currentPlayer = 'X';
        this.gameOver = false;
        this.human = 'X';
        this.ai = 'O';
        this.boardElement = document.getElementById('board');
        this.statusEl = document.getElementById('status');
        this.resetBtn = document.getElementById('resetBtn');
        this.timerId = null;
        this.initBoard();
        this.setupEvents();
    }

    initBoard() {
        this.boardElement.innerHTML = '';
        for (let i = 0; i < 9; i++) {
            const cell = document.createElement('div');
            cell.classList.add('cell');
            cell.dataset.index = i;
            cell.addEventListener('click', () => this.handleCellClick(i));
            this.boardElement.appendChild(cell);
        }
    }

    setupEvents() {
        this.resetBtn.addEventListener('click', () => this.reset());
    }

    handleCellClick(index) {
        // Blocca gli input quando non è il turno del giocatore umano o se game over
        if (this.currentPlayer !== this.human || this.gameOver) return;

        const cell = this.boardElement.children[index];
        if (cell.textContent) return; // cella già occupata

        // Umano gioca X
        this.board[index] = this.human;
        cell.textContent = 'X';
        cell.classList.add('x');

        let result = null;
        if (this.checkWin(this.human)) {
            result = 'Hai vinto! 🎉';
        } else if (!this.board.includes(null)) {
            // Tabella piena, pareggio
            result = 'Pareggio';
        }

        if (result) {
            this.endGame(result);
            return;
        }

        this.currentPlayer = this.ai;
        this.statusEl.textContent = 'Turno del PC (O)';

        // Salvare ID timeout e cancellarlo in caso di reset
        const self = this;
        this.timerId = setTimeout(() => {
            clearTimeout(self.timerId);
            self.aiMove();
        }, 300);
    }

    aiMove() {
        if (this.gameOver) return;

        const move = this.getBestMove();
        if (move !== -1) {
            this.board[move] = this.ai;
            const cell = this.boardElement.children[move];
            cell.textContent = 'O';
            cell.classList.add('o');

            let result = null;
            if (this.checkWin(this.ai)) {
                result = 'Il PC ha vinto! 😱';
            } else if (!this.board.includes(null)) {
                result = 'Pareggio';
            }

            if (result) {
                this.endGame(result);
                return;
            }
        }

        this.currentPlayer = 'X';
        this.statusEl.textContent = 'Il tuo turno! Clicca su una casella.';
    }

    reset() {
        // Cancellare il timer in corso prima di resettare
        clearTimeout(this.timerId);
        this.board = Array(9).fill(null);
        this.gameOver = false;
        for (let i = 0; i < 9; i++) {
            const cell = this.boardElement.children[i];
            cell.textContent = '';
            cell.className = 'cell';
        }
        this.currentPlayer = 'X';
        this.statusEl.textContent = 'Il tuo turno! Clicca su una casella.';
    }

    endGame(result) {
        this.gameOver = true;
        if (result === 'Hai vinto! 🎉') {
            this.statusEl.textContent = result;
        } else if (result === 'Il PC ha vinto! 😱') {
            this.statusEl.textContent = result;
        } else if (result === 'Pareggio') {
            this.statusEl.textContent = 'La partita è finita — pareggio';
        }
    }

    getBestMove() {
        let bestScore = -Infinity;
        let move = -1;
        for (let i = 0; i < 9; i++) {
            if (!this.board[i]) {
                this.board[i] = this.ai;
                const score = this.minimax(this.board, 0, false);
                this.board[i] = null;
                if (score > bestScore) {
                    bestScore = score;
                    move = i;
                }
            }
        }
        return move;
    }

    minimax(board, depth, isMaximizing) {
        const winner = this.checkWinnerForMinimax();
        if (winner === 'X') return -10 + depth;
        if (winner === 'O') return 10 - depth;
        if (!board.includes(null)) return 0;

        if (isMaximizing) {
            let best = -Infinity;
            for (let i = 0; i < 9; i++) {
                if (!board[i]) {
                    board[i] = 'O';
                    best = Math.max(best, this.minimax(board, depth + 1, false));
                    board[i] = null;
                }
            }
            return best;
        } else {
            let best = Infinity;
            for (let i = 0; i < 9; i++) {
                if (!board[i]) {
                    board[i] = 'X';
                    best = Math.min(best, this.minimax(board, depth + 1, true));
                    board[i] = null;
                }
            }
            return best;
        }
    }

    checkWinnerForMinimax() {
        const winPatterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ];
        for (const pattern of winPatterns) {
            const [a, b, c] = pattern;
            // Corretto: confronta esplicitamente tutte e tre le celle
            if (this.board[a] === this.ai && this.board[b] === this.ai && this.board[c] === this.ai) {
                return this.ai;
            }
        }
        return null;
    }

    checkWin(player) {
        const winPatterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ];
        for (const pattern of winPatterns) {
            const [a, b, c] = pattern;
            if (this.board[a] === player && this.board[b] === player && this.board[c] === player) {
                return true;
            }
        }
        return false;
    }
}

// Istanziazione del gioco: risolve il blocco all'avvio (il DOM deve esistere)
new TicTacToe();
