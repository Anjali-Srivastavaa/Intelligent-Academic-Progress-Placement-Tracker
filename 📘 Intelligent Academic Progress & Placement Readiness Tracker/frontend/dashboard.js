async function loadScore() {
    const studentId = document.getElementById("student_id").value;
    const resultCard = document.getElementById("result-card");
    const scoreValue = document.getElementById("score-value");
    const cgpaValue = document.getElementById("cgpa-value");
    const skillsValue = document.getElementById("skills-value");

    if (!studentId) {
        alert("Please enter a valid Student ID");
        return;
    }

    try {
        const res = await fetch(`http://127.0.0.1:5000/analytics/readiness/${studentId}`);
        
        if (!res.ok) {
            const error = await res.json();
            alert(error.message || "Failed to fetch score");
            resultCard.style.display = "none";
            return;
        }

        const data = await res.json();
        
        // Update values in the UI
        scoreValue.innerText = data.placement_score.toFixed(2);
        cgpaValue.innerText = data.cgpa;
        skillsValue.innerText = data.skills_count;
        
        // Show the result card
        resultCard.style.display = "block";

    } catch (err) {
        console.error("Error fetching score:", err);
        alert("Server is not responding. Make sure the Flask backend is running on http://127.0.0.1:5000");
    }
}
