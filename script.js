function startQuiz() {
    document.getElementById("menu").style.display = "none"; // hide menu
    document.getElementById("quiz").style.display = "block"; // show quiz
}

async function submitQuiz() {
    const q1 = document.getElementById("q1").value.trim();
    const q2 = document.getElementById("q2").value.trim();
    const q3 = document.getElementById("q3").value.trim();
    let q4 = document.getElementById("q4").value.trim().toLowerCase();
    const q5 = document.getElementById("q5").value.trim();

    if (q4 !== "yes" && q4 !== "no") {
        alert("Please answer Q4 with 'yes' or 'no'.");
        return;
    }

    const answers = [q1, q2, q3, q4, q5];

    // Call Python backend
    const result = await window.pywebview.api.start(answers);

    // Display result
    document.getElementById("result").innerText = result;
}