// عند تحميل الصفحة
document.addEventListener("DOMContentLoaded", () => {
  loadFaculty();

  document.getElementById("addForm").addEventListener("submit", function (e) {
      e.preventDefault();
      addFaculty();
  });

  document.getElementById("logoutBtn").addEventListener("click", logout);
});

async function loadFaculty() {
  const response = await fetch("http://127.0.0.1:5000/faculty");
  const data = await response.json();

  const table = document.getElementById("facultyTable");
  table.innerHTML = "<tr><th>ID</th><th>Name</th><th>Department</th><th>Actions</th></tr>";

  data.forEach(member => {
      const row = document.createElement("tr");
      row.innerHTML = `
          <td>${member.id}</td>
          <td>${member.name}</td>
          <td>${member.department}</td>
          <td><button onclick="deleteFaculty('${member.id}')">Delete</button></td>
      `;
      table.appendChild(row);
  });
}

async function addFaculty() {
  const id = document.getElementById("id").value;
  const name = document.getElementById("name").value;
  const department = document.getElementById("department").value;
  const courses = document.getElementById("courses").value;
  const fields = document.getElementById("fields").value;
  const interests = document.getElementById("interests").value;

  const response = await fetch("http://127.0.0.1:5000/faculty", {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify({
          id, name, department,
          coursesTaught: courses,
          fieldsOfSpeciality: fields,
          professionalInterests: interests
      })
  });

  const result = await response.json();
  alert(result.message);
  loadFaculty();
}

async function deleteFaculty(id) {
  const response = await fetch(http://127.0.0.1:5000/faculty/${id}, {
      method: "DELETE"
  });
  const result = await response.json();
  alert(result.message);
  loadFaculty();
}

async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const response = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify({ username, password })
  });

  if (response.ok) {
      window.location.href = "main.html";
  } else {
      const result = await response.json();
      alert(result.message);
  }
}

async function logout() {
  const response = await fetch("http://127.0.0.1:5000/logout", {
      method: "POST"
  });
  const result = await response.json();
  alert(result.message);
  window.location.href = "login.html";
}