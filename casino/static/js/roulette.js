const choiceInput = document.getElementById("choice-input");
const selectedBet = document.getElementById("selected-bet");
const betButtons = document.querySelectorAll("[data-choice]");

betButtons.forEach(button => {
    button.addEventListener("click", function () {
        choiceInput.value = this.dataset.choice;
        selectedBet.textContent = "Selected Bet: " + this.dataset.choice;

        betButtons.forEach(btn => btn.classList.remove("selected"));
        this.classList.add("selected");
    });
});

document.getElementById("roulette-form").addEventListener("submit", function(event) {
    if (!choiceInput.value) {
        event.preventDefault();
        alert("Please click a bet first.");
    }
});