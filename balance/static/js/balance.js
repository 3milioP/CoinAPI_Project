
const petition = new XMLHttpRequest();

function loadMovements() {

    // let queryParams = getQueryParams();

    let url = 'http://127.0.0.1:5000//api/v1/movements';

    // if (queryParams) {
    //     url += '?' + queryParams;
    // }

    petition.open('GET', url, false);
    petition.send();

    const table = document.getElementById('cuerpo-tabla')
    console.log(table.innerHTML)
    const html = '<tr><td>05 / 07 / 2022';
    table.innerHTML += html;
};

// function getQueryParams() {
//     const params = new URLSearchParams(window.location.search);

//     let queryParams = '';

//     if (params.has('p') && params.get('p')) {
//         queryParams = `p=${params.get('p')}`;
//     }

//     if (params.has('r') && params.get('r')) {
//         if (queryParams) {
//             queryParams += '&';
//         }
//         queryParams += `r=${params.get('r')}`;
//     }

//     console.log('queryParams', queryParams);
//     return queryParams;
// }

// function deleteMovement(event) {
//     const target = event.target;
//     const id = target.getAttribute('data-id');
//     fetch(`http://localhost:5000/api/v1/movements/${id}`, {
//         method: 'DELETE',
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     })
//         .then((response) => {
//             if (response.status === 204) {
//                 alert('The movement has been delete succesfully.');
//                 showMovements();
//                 // FIXME: Simplemente eliminar la línea del movimiento (sin recargarlos todos)
//             } else {
//                 alert('ERROR: Fail in delete movement.');
//             }
//         })
//         .catch(
//             (error) => alert('UNKNOWN ERROR on movement delete (API)')
//         );

// }

// function showMovements() {

//     if (this.readyState === 4 && this.status === 200) {
//         console.log('---- TODO OK ----');
//         const response = JSON.parse(petition.responseText);
//         const movements = response.results;

//         let html = '';
//         for (let i = 0; i < movements.length; i = i + 1) {
//             const mov = movements[i];

//             // Fecha en formato ES
//             const date = new Date(mov.date);
//             // puedo pasar la cultura es-ES o dejar que use la que tiene por defecto
//             const formatDate = date.toLocaleDateString();

//             // Ajustar los decimales de la cantidad
//             const options = {
//                 minimumFractionDigits: 2,
//                 maximumFractionDigits: 2
//             };
//             const formatter = new Intl.NumberFormat('es-ES', options);
//             const from_quantity = formatter.format(mov.from_quantity);
//             const to_quantity = formatter.format(mov.to_quantity);

//             // const laCantidad = mov.cantidad.toLocaleString();
//             // const laCantidad = mov.cantidad.toFixed(2);

//             html = html + `
//         <tr>
//           <td class="date">${formatDate}</td>
//           <td>${mov.from_currency}</td>
//           <td class="number">${from_quantity}</td>
//           <td>${mov.to_currency}</td>
//           <td class="number">${to_quantity}</td>
//           <td class="acciones">
//             <a class="link-icon btn-delete">
//               <i class="fa-solid fa-trash" data-id="${mov.id}"></i>
//             </a>
//             <a href="/modificar/${mov.id}" class="link-icon">
//               <i class="fa-solid fa-pen-to-square"></i>
//             </a>
//         </td>
//         </tr>
//       `;
//         }

//         const table = document.querySelector('#cuerpo-tabla');
//         table.innerHTML = html;

//     } else {
//         console.error('---- Algo ha ido mal en la petición ----');
//         alert('Error al cargar los movimientos');
//     }

// }



// window.onload = function () {
//     showMovements();
//     petition.onload = showMovements;
// };