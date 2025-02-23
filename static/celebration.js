document.addEventListener("DOMContentLoaded", function() {
    function createConfetti() {
        const confetti = document.createElement("div");
        confetti.classList.add("confetti");
        document.body.appendChild(confetti);

        confetti.style.left = Math.random() * 100 + "vw";
        confetti.style.animationDuration = Math.random() * 2 + 3 + "s";

        setTimeout(() => {
            confetti.remove();
        }, 5000);
    }

    for (let i = 0; i < 100; i++) {
        createConfetti();
    }
});
