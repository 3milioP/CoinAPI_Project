

function loadMovements() {

  let queryParams = getQueryParams();

  let url = 'http://localhost:5000/api/v1/movements';

  if (queryParams) {
    url += '?' + queryParams;
  }

  fetch(url)
    .then(response => response.json())
    .then(response => {

      const options = {
        minimumFractionDigits: 3,
        maximumFractionDigits: 3
      };
      const formatter = new Intl.NumberFormat('es-ES', options);

      const movements = response.results;
      let html = '';
      if (movements && movements.length > 0) {

        for (const mov of movements) {
          mov.u_price = mov.from_quantity / mov.to_quantity
          html += `
                  <tr>
                    <td>${mov.date}</td>
                    <td>${mov.time}</td>
                    <td>${mov.from_currency}</td>
                    <td>${formatter.format(mov.from_quantity)}</td>
                    <td>${mov.to_currency}</td>
                    <td>${formatter.format(mov.to_quantity)}</td>
                    <td>${formatter.format(mov.u_price)}</td>
                  </tr>
                `;
        }
      } else {
        html = 'NO MOVEMENTS'
      }

      const table = document.querySelector('#table-container');
      table.innerHTML += html;
    })
    .catch((error) => console.log('ERROR: Data load failed', error));
}

function getQueryParams() {
  const params = new URLSearchParams(window.location.search);

  let queryParams = '';

  if (params.has('p') && params.get('p')) {
    queryParams = `p=${params.get('p')}`;
  }

  if (params.has('r') && params.get('r')) {
    if (queryParams) {
      queryParams += '&';
    }
    queryParams += `r=${params.get('r')}`;
  }

  console.log('queryParams', queryParams);
  return queryParams;
}

window.addEventListener('load', loadMovements);

window.onload = function () {
  balanceNav = document.getElementById('balance')
  balanceNav.style.pointerEvents = "none"
  balanceNav.style.color = "#999";
}
