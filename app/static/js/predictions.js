function launchConfetti() {
    const confettiCanvas = document.getElementById('confetti-canvas');
    confetti.create(confettiCanvas, {
        resize: true, // Redimensionne automatiquement avec la fenêtre
        useWorker: true, // Utilise un worker pour de meilleures performances
    })({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 },
        colors: ["#ff0a54", "#ff477e", "#ff7096", "#ff85a1", "#fbb1bd", "#f9bec7"]
    });
}

// Affiche la pop-up avec l'animation de confettis
document.getElementById("predict-button").addEventListener("click", function(event) {
    event.preventDefault(); // Empêche le rechargement de la page

    // Récupère les données du formulaire
    const formData = new FormData(document.getElementById("predict-form"));
    const data = Object.fromEntries(formData.entries());

    // Envoie une requête asynchrone à l'API
    fetch("/api/v1/predict-nutriscore", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        // Affiche le résultat dans la pop-up
        document.getElementById("result-popup").style.display = "flex";
        document.getElementById("popup-predicted-score").textContent = result.prediction;
        document.getElementById("popup-nutriscore-image").src = `/static/images/nutriscore-${result.prediction}-new-en.svg`;

        // Lancer les confettis lors de l'affichage de la pop-up
        launchConfetti()
    })
    .catch(error => {
        console.error("Error:", error);
    });
});

// Bouton pour réinitialiser le formulaire
document.getElementById("reset-button").addEventListener("click", function() {
    document.getElementById("predict-form").reset();
    document.getElementById("result-popup").style.display = "none";
});

// Bouton pour garder les valeurs actuelles et revenir au formulaire
document.getElementById("keep-values-button").addEventListener("click", function() {
    document.getElementById("result-popup").style.display = "none";
});
