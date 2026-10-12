
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
