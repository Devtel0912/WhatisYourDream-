async function submitQuiz() {
    const Q1 = document.getElementById("Q1").value.trim();
    const Q2 = document.getElementById("Q2").value.trim();
    const Q3 = document.getElementById("Q3").value.trim();
    let Q4 = document.getElementById("Q4").value.trim().toLowerCase();
    const Q5 = document.getElementById("Q5").value.trim();

    // Ensure Q4 is yes or no
    if (Q4 !== "yes" && Q4 !== "no") {
        alert("Please answer Q4 with 'yes' or 'no'.");
        return;
    }

    const answers = [Q1, Q2, Q3, Q4, Q5];

    // Call Python backend
    const result = await window.pywebview.api.start(answers);

    // Display result
    document.getElementById("result").innerText = result;
}