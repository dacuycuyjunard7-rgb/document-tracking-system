
const searchInput = document.getElementById("document-search");
const table = document.getElementById("documents-table");
const emptyMessage = document.getElementById("empty-search");

if (searchInput && table && emptyMessage) {
    const rows = Array.from(table.querySelectorAll("tbody tr"));

    searchInput.addEventListener("input", () => {
        const query = searchInput.value.trim().toLowerCase();
        let visibleRows = 0;

        rows.forEach((row) => {
            const matches = row.textContent.toLowerCase().includes(query);
            row.hidden = !matches;

            if (matches) {
                visibleRows++;
            }
        });

        emptyMessage.hidden = visibleRows !== 0;
    });
}

const registerButton = document.getElementById("register-document");

if (registerButton) {
    registerButton.addEventListener("click", () => {
        alert("The document registration form will be implemented next.");
    });
}


function toggleCourseMenu() {
    const menu = document.getElementById("course-menu");
    const arrow = document.getElementById("course-arrow");

    if (!menu || !arrow) return;

    const isHidden = menu.style.display === "none";
    menu.style.display = isHidden ? "block" : "none";
    arrow.textContent = isHidden ? "▴" : "▾";
}
