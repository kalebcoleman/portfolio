document.addEventListener("DOMContentLoaded", () => {
    const chartDataNode = document.getElementById("chart-data");

    if (!chartDataNode || typeof Chart === "undefined") {
        return;
    }

    const chartData = JSON.parse(chartDataNode.textContent || "{}");
    const courseCanvas = document.getElementById("courseMixChart");
    const archetypeCanvas = document.getElementById("archetypeChart");

    if (!(courseCanvas instanceof HTMLCanvasElement) || !(archetypeCanvas instanceof HTMLCanvasElement)) {
        return;
    }

    new Chart(courseCanvas, {
        type: "doughnut",
        data: {
            labels: chartData.course_mix.labels,
            datasets: [
                {
                    data: chartData.course_mix.values,
                    backgroundColor: ["#2d8cff", "#9db1c8"],
                    borderColor: ["#ffffff", "#ffffff"],
                    borderWidth: 2,
                },
            ],
        },
        options: {
            plugins: {
                legend: {
                    labels: { color: "#102a43" },
                },
            },
        },
    });

    new Chart(archetypeCanvas, {
        type: "bar",
        data: {
            labels: chartData.shot_archetypes.labels,
            datasets: [
                {
                    label: "Count",
                    data: chartData.shot_archetypes.values,
                    borderRadius: 8,
                    backgroundColor: ["#2d8cff", "#66b3ff", "#f2a900", "#4fac82", "#6f86a7"],
                },
            ],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { color: "#102a43" },
                    grid: { color: "rgba(16, 42, 67, 0.15)" },
                },
                x: {
                    ticks: { color: "#102a43" },
                    grid: { color: "rgba(16, 42, 67, 0.1)" },
                },
            },
            plugins: {
                legend: {
                    labels: { color: "#102a43" },
                },
            },
        },
    });
});
