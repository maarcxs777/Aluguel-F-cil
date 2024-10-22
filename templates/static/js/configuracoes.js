document.addEventListener("DOMContentLoaded", function() {
    const themeSelect = document.getElementById("theme");
    const customThemeOptions = document.getElementById("customThemeOptions");

    // Carrega o tema armazenado no localStorage
    const storedTheme = localStorage.getItem("theme");
    if (storedTheme) {
        document.body.classList.toggle("dark-mode", storedTheme === "dark");
        themeSelect.value = storedTheme;
    }

    themeSelect.addEventListener("change", function() {
        if (this.value === "dark") {
            document.body.classList.add("dark-mode");
            localStorage.setItem("theme", "dark"); // Armazena o tema
        } else if (this.value === "light") {
            document.body.classList.remove("dark-mode");
            localStorage.setItem("theme", "light"); // Armazena o tema
        } else {
            customThemeOptions.style.display = "block"; // Exibe opções personalizadas
        }
    });
});
