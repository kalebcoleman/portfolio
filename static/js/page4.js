document.addEventListener("DOMContentLoaded", () => {
    const toggleButtons = document.querySelectorAll(".toggle-button[data-target]");

    toggleButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const targetId = button.getAttribute("data-target");
            const panel = targetId ? document.getElementById(targetId) : null;

            if (!panel) {
                return;
            }

            const expanded = button.getAttribute("aria-expanded") === "true";
            const nextExpanded = !expanded;
            const showLabel = button.getAttribute("data-show-label") || "Show";
            const hideLabel = button.getAttribute("data-hide-label") || "Hide";

            button.setAttribute("aria-expanded", String(nextExpanded));
            button.textContent = nextExpanded ? hideLabel : showLabel;
            panel.hidden = !nextExpanded;
        });
    });
});
