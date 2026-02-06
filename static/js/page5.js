document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("toolbox-form");
    const queryInput = document.getElementById("query-input");
    const responseEl = document.getElementById("toolbox-response");

    if (!(form instanceof HTMLFormElement) || !(queryInput instanceof HTMLInputElement) || !responseEl) {
        return;
    }

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const query = queryInput.value.trim();
        if (!query) {
            responseEl.innerHTML = "<p>Please enter a query.</p>";
            return;
        }

        responseEl.innerHTML = "<p>Querying API...</p>";

        try {
            const response = await fetch("/api/toolbox/query", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query }),
            });

            if (!response.ok) {
                throw new Error(`status ${response.status}`);
            }

            const data = await response.json();
            responseEl.innerHTML = `
                <p><strong>Tool:</strong> ${data.matched_tool}</p>
                <p><strong>Suggestion:</strong> ${data.suggestion}</p>
                <p><strong>Example:</strong> <code>${data.example_call}</code></p>
            `;
        } catch (error) {
            responseEl.innerHTML = `<p>Request failed: ${error.message}</p>`;
        }
    });
});
