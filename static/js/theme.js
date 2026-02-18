(() => {
    const THEME_KEY = "theme";
    const LIGHT = "light";
    const DARK = "dark";

    const mediaQuery = window.matchMedia
        ? window.matchMedia("(prefers-color-scheme: light)")
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
        return mediaQuery?.matches ? LIGHT : DARK;
    };

    const applyTheme = (theme) => {
        const root = document.documentElement;
        if (theme === LIGHT) {
            root.setAttribute("data-theme", LIGHT);
        } else {
            root.setAttribute("data-theme", DARK);
        }

        const iconNode = document.getElementById("theme-toggle-icon");
        const toggleButton = document.getElementById("theme-toggle");
        if (iconNode) {
            iconNode.textContent = theme === LIGHT ? "☀" : "🌙";
        }
        if (toggleButton) {
            toggleButton.setAttribute("aria-pressed", theme === LIGHT ? "true" : "false");
            toggleButton.setAttribute(
                "aria-label",
                theme === LIGHT ? "Switch to dark mode" : "Switch to light mode"
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
        const initialTheme = getPreferredTheme();
        applyTheme(initialTheme);

        const toggleButton = document.getElementById("theme-toggle");
        if (toggleButton) {
            toggleButton.addEventListener("click", () => {
                const current = document.documentElement.getAttribute("data-theme") === LIGHT ? LIGHT : DARK;
                const nextTheme = current === LIGHT ? DARK : LIGHT;
                applyTheme(nextTheme);
                persistTheme(nextTheme);
            });
        }

        if (mediaQuery?.addEventListener) {
            mediaQuery.addEventListener("change", (event) => {
                if (getStoredTheme()) {
                    return;
                }
                applyTheme(event.matches ? LIGHT : DARK);
            });
        }
    };

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initialize);
    } else {
        initialize();
    }
})();
