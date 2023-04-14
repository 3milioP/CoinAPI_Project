function loadMovements() {
    fetch('http://localhost:5000/api/v1/movements/status')
        .then(response => response.json())
        .then(response => {
            const invStatus = response.total_euros_invested
            const actualValue = response.euro_wallet_amount
            console.log(invStatus, actualValue)

            let html = '';
            if (invStatus) {
                html += `
                    <tr>
                    <td>${invStatus}</td>
                    <td>${actualValue}</td>
                    </tr>
                    `;
            } else {
                html = 'You have no inversion yet'
            }
            const table = document.querySelector('#inv-status');
            table.innerHTML += html;
        })
        .catch((error) => console.log('ERROR: Data load failed', error));
}

window.onload = function () {
    statusNav = document.getElementById('status');
    statusNav.style.pointerEvents = "none";
    statusNav.style.color = "#999";
    loadMovements();
}


