async function fetchFacultyData() {
    try {
        const response = await fetch('http://127.0.0.1:5000/faculty');  // رابط API لفئة faculty
        const data = await response.json();
        loadTable(data);
    } catch (error) {
        console.error('Error fetching faculty data:', error);
    }
}

function loadTable(data) {
    const tbody = document.getElementById("facultyBody");
    tbody.innerHTML = "";
    data.forEach(person => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${person.name}</td>
            <td>${person.department}</td>
            <td>—</td>
            <td>—</td>
            <td>—</td>
            <td>—</td>
        `;
        tbody.appendChild(row);
    });
}

function performSearch() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const rows = document.querySelectorAll("#facultyBody tr");

    rows.forEach(row => {
        const text = row.innerText.toLowerCase();
        if (text.includes(input)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}

document.getElementById("searchInput").addEventListener("keyup", async function () {
    const query = this.value.toLowerCase();
    try {
        const response = await fetch('http://127.0.0.1:5000/faculty/search', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name: query,
                department: '',
                course: '',
                speciality: '',
                intersts: ''
            })
        });
        const results = await response.json();
        loadTable(results);
    } catch (error) {
        console.error('Search error:', error);
    }
});

window.onload = fetchFacultyData;
