const simulatedData = [
    { name: "John Doe", gender: "male", age: 55, condition: "diabetes" },
    { name: "Jane Smith", gender: "female", age: 34, condition: "hypertension" },
    { name: "Alice Johnson", gender: "female", age: 65, condition: "asthma" },
    { name: "Bob Brown", gender: "male", age: 72, condition: "diabetes" },
    { name: "Charlie Davis", gender: "male", age: 46, condition: "hypertension" },
    { name: "Emily Clark", gender: "female", age: 29, condition: "asthma" },
    { name: "Frank Miller", gender: "male", age: 61, condition: "diabetes" },
    { name: "Grace Lee", gender: "female", age: 38, condition: "hypertension" },
    { name: "Henry Wilson", gender: "male", age: 50, condition: "asthma" },
    { name: "Irene Kim", gender: "female", age: 43, condition: "diabetes" },
    { name: "Jack White", gender: "male", age: 67, condition: "hypertension" },
    { name: "Karen Young", gender: "female", age: 52, condition: "asthma" },
    { name: "Leo Turner", gender: "male", age: 60, condition: "diabetes" },
    { name: "Mia Scott", gender: "female", age: 33, condition: "hypertension" },
    { name: "Noah Hall", gender: "male", age: 48, condition: "asthma" }
];

function handleQuery() {
    const query = document.getElementById('queryInput').value.toLowerCase();

    let filteredData = filterData(query);

    // Update the table with the filtered data
    updateTable(filteredData);

    // Update the chart with the filtered data
    updateChart(filteredData);
}

// Function to filter data based on the query (for simplicity)
function filterData(query) {
    // Example filtering based on query content
    let filteredData = simulatedData;

    if (query.includes(" male") || query.includes(" men")) {
        filteredData = filteredData.filter(patient => patient.gender === "male");
    }

    if (query.includes("female") || query.includes("women")) {
        filteredData = filteredData.filter(patient => patient.gender === "female");
    }

    if (query.includes("over")) {
        const ageLimit = parseInt(query.match(/over (\d+)/)?.[1] || 0);
        filteredData = filteredData.filter(patient => patient.age > ageLimit);
    }

    if (query.includes("above")) {
        const ageLimit = parseInt(query.match(/above (\d+)/)?.[1] || 0);
        filteredData = filteredData.filter(patient => patient.age > ageLimit);
    }

    if (query.includes("under")) {
        const ageLimit = parseInt(query.match(/under (\d+)/)?.[1] || 0);
        filteredData = filteredData.filter(patient => patient.age < ageLimit);
    }

    if (query.includes("below")) {
        const ageLimit = parseInt(query.match(/below (\d+)/)?.[1] || 0);
        filteredData = filteredData.filter(patient => patient.age < ageLimit);
    }

    if (query.includes("diabetic") || query.includes("diabetes")) {
        filteredData = filteredData.filter(patient => patient.condition === "diabetes");
    }

    if (query.includes("hypertension")) {
        filteredData = filteredData.filter(patient => patient.condition === "hypertension");
    }

    if (query.includes("asthma") || query.includes("asthmatic")) {
        filteredData = filteredData.filter(patient => patient.condition === "asthma");
    }

    return filteredData;
}

// Function to update the table with filtered data
function updateTable(data) {
    const tableBody = document.querySelector("#resultsTable tbody");
    tableBody.innerHTML = ""; // Clear previous table rows

    data.forEach(patient => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${patient.name}</td>
            <td>${patient.gender}</td>
            <td>${patient.age}</td>
            <td>${patient.condition}</td>
        `;
        tableBody.appendChild(row);
    });
}

// Function to update the chart with filtered data
function updateChart(data) {
    const chartCanvas = document.getElementById("chartCanvas");
    const ctx = chartCanvas.getContext("2d");

    // Prepare data for the pie chart (condition distribution)
    const conditionCounts = data.reduce((acc, patient) => {
        acc[patient.condition] = (acc[patient.condition] || 0) + 1;
        return acc;
    }, {});

    const chartData = {
        labels: Object.keys(conditionCounts),
        datasets: [{
            data: Object.values(conditionCounts),
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
        }],
    };

    if (window.chart) {
        window.chart.destroy();
    }

    window.chart = new Chart(ctx, {
        type: 'pie',
        data: chartData,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return `${tooltipItem.label}: ${tooltipItem.raw} patients`;
                        }
                    }
                }
            }
        }
    });
}