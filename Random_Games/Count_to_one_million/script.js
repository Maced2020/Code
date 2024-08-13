let currentNumber = 0;
const numberDisplay = document.getElementById('numberDisplay');
const winnerText = document.getElementById('winnerText');

function increaseNumber() {
    if (currentNumber < 1000000) {
        currentNumber++;
        updateDisplay();
    }
    if (currentNumber === 1000000) {
        winnerText.textContent = "Winner!";
        winnerText.classList.remove('hidden');
    } else if (winnerText.textContent === "Winner!" && currentNumber !== 1000000) {
        winnerText.classList.add('hidden');
    }
}

function decreaseNumber() {
    if (currentNumber > -1000000) {
        currentNumber--;
        updateDisplay();
    }
    if (currentNumber === -1000000) {
        winnerText.textContent = "Loser!";
        winnerText.classList.remove('hidden');
    } else if (winnerText.textContent === "Loser!" && currentNumber !== -1000000) {
        winnerText.classList.add('hidden');
    }
}

function updateDisplay() {
    numberDisplay.textContent = currentNumber;
}
