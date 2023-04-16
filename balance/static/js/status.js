function loadMovements() {
    fetch('http://localhost:5000/api/v1/movements/data')
        .then(response => response.json())
        .then(response => {
            const invStatus = response.total_euros_invested
            const actualValue = response.euro_wallet_amount
            const withdrawed = response.withdrawed
            const options = {
                minimumFractionDigits: 3,
                maximumFractionDigits: 3
            };
            const formatter = new Intl.NumberFormat('es-ES', options);
            let html = '';
            if (invStatus) {
                html += `
                    <tr>
                    <td>${formatter.format(invStatus)}</td>
                    <td>${formatter.format(actualValue)}</td>
                    <td>${formatter.format(withdrawed)}</td>
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


