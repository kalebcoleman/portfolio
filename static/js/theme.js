(() => {
    const THEME_KEY = "theme";
    const LIGHT = "light";
    const DARK = "dark";

    const mediaQuery = window.matchMedia
        ? window.matchMedia("(prefers-color-scheme: dark)")
        : null;

    const getStoredTheme = () => {
        try {
            const value = localStorage.getItem(THEME_KEY);
            return value === LIGHT || value === DARK ? value : null;
        } catch {
            return null;
        }
    };

    const getPreferredTheme = () => {
        const storedTheme = getStoredTheme();
        if (storedTheme) {
            return storedTheme;
        }
        return mediaQuery?.matches ? DARK : LIGHT;
    };

    const applyTheme = (theme) => {
        document.documentElement.setAttribute("data-theme", theme);

        const iconNode = document.getElementById("theme-toggle-icon");
        const toggleButton = document.getElementById("theme-toggle");
        const isDark = theme === DARK;

        if (iconNode) {
            iconNode.textContent = isDark ? "☾" : "☀";
        }

        if (toggleButton) {
            toggleButton.setAttribute("aria-pressed", isDark ? "true" : "false");
            toggleButton.setAttribute(
                "aria-label",
                isDark ? "Switch to light mode" : "Switch to dark mode"
            );
        }
    };

    const persistTheme = (theme) => {
        try {
            localStorage.setItem(THEME_KEY, theme);
        } catch {
            return;
        }
    };

    const initialize = () => {
        applyTheme(getPreferredTheme());

        const toggleButton = document.getElementById("theme-toggle");
        if (toggleButton) {
            toggleButton.addEventListener("click", () => {
                const current = document.documentElement.getAttribute("data-theme") === DARK ? DARK : LIGHT;
                const nextTheme = current === DARK ? LIGHT : DARK;
                applyTheme(nextTheme);
                persistTheme(nextTheme);
            });
        }

        if (mediaQuery?.addEventListener) {
            mediaQuery.addEventListener("change", (event) => {
                if (getStoredTheme()) {
                    return;
                }
                applyTheme(event.matches ? DARK : LIGHT);
            });
        }
    };

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initialize);
    } else {
        initialize();
    }
})();
