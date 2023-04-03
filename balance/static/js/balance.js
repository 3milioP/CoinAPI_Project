function loadMovements() {

  fetch('http://localhost:5000/api/v1/movements')
    .then(response => response.json())
    .then(response => {
      const movements = response.results;

      let html = '';
      for (let i = 0; i < movements.length; i = i + 1) {
        const mov = movements[i];
        html += `
                  <tr>
                    <td>${mov.date}</td>
                    <td>${mov.time}</td>
                    <td>${mov.from_currency}</td>
                    <td>${mov.from_quantity}</td>
                    <td>${mov.to_currency}</td>
                    <td>${mov.to_quantity}</td>
                    <td>${mov.u_price}</td>
                  </tr>
                `;
      }

      const table = document.querySelector('#table-body');
      table.innerHTML += html;
    })
    .catch((error) => console.log('ERROR: Data load failed', error));
}

window.addEventListener('load', loadMovements);
