document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".collect-buttons button[data-url]").forEach(btn => {
      btn.addEventListener("click", () => {
        const url = btn.getAttribute("data-url");
        if (url) window.location.href = url;
      });
    });
  });

document.addEventListener("DOMContentLoaded", function() {
  // Injecte les styles CSS dynamiquement
  const cssRules = `
    .login-container {
      background: rgba(255, 255, 255, 1);
      backdrop-filter: blur(8px);
      padding: 2rem;
      max-width: 360px;
      margin: 2rem auto;
      border-radius: 12px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
      color: #333;
    }
    .login-container h3 {
      text-align: center;
      font-style: italic;
      margin-bottom: 1rem;
      color: #1A5276;
    }
    .form-group { margin-bottom: 1rem; }
    .form-group label {
      display: block;
      color: #555;
      margin-bottom: 0.3rem;
    }
    .form-group input {
      width: 100%;
      height: 40px;
      border: none;
      border-radius: 6px;
      background: rgb(197, 237, 253);
      color: #333;
    }
    .login-button {
      width: 100%;
      height: 40px;
      border: none;
      border-radius: 6px;
      background: #007BFF;
      color: #fff;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.3s, transform 0.2s;
    }
    .login-button:hover {
      background: #0056b3;
      transform: translateY(-2px);
    }
  `;
  const styleEl = document.createElement("style");
  styleEl.type = "text/css";
  styleEl.innerText = cssRules;
  document.head.appendChild(styleEl);

  // Gestion des clics et génération du formulaire
  const container = document.getElementById("form-container");
  document.querySelectorAll(".collect-buttons button").forEach(btn => {
    btn.addEventListener("click", () => {
      const label = btn.textContent.trim();
      container.innerHTML = `
        <div class="login-container">
          <h3> Connexion — ${label}</h3>
          <form>
            <div class="form-group">
              <label>Login</label>
              <input type="text" name="username" required>
            </div>
            <div class="form-group">
              <label>Mot de passe</label>
              <input type="password" name="password" required>
            </div>
            <button type="submit" class="login-button">Entrer</button>
          </form>
        </div>`;
      container.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  });
});

