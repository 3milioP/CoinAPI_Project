console.log('--- Iniciamos ejecución de form.js ---');

const form = document.getElementById('form-mov');
const calculate = document.getElementById('calculate')

form.addEventListener('submit', sendForm);
calculate.addEventListener('click', calculateForm);

function calculateForm() {

    let from_currency = document.getElementById("from_currency");
    origin = from_currency.options[from_currency.selectedIndex].value;

    let to_currency = document.getElementById("to_currency");
    destiny = to_currency.options[to_currency.selectedIndex].value;

    let from_quantity = document.getElementById("from_quantity");
    quant = from_quantity.value;

    fetch(`https://rest.coinapi.io/v1/exchangerate/${origin}/${destiny}`, {
        method: "GET",
        headers: {
            'X-CoinAPI-Key': 'E6A881EC-A489-4A17-BD9D-354A4625D54A'
        }
    })
        .then(response => response.json())
        .then(response => {
            const ex_rate = response.rate

            quantity = document.getElementById("to_quantity")
            quantity.value = ex_rate * quant

            let u_price = document.getElementById("u_price");
            u_price.value = ex_rate

        })
}
function sendForm(event) {
    console.log('Form sended', event);
    event.preventDefault();


    const formData = new FormData(form);
    console.log('formData', formData);

    const jsonData = {};
    formData.forEach((value, key) => jsonData[key] = value);
    console.log('1. JSON', jsonData);

    let operacion;
    let url;

    operacion = 'POST';
    url = 'http://127.0.0.1:5000//api/v1/movements';

    fetch(url, {
        method: operacion,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
        .then(
            (response) => {
                console.log('2.', response);
                return response.json();
            }
        )
        .then((data) => {
            console.log('3.', data);
            if (data.status === 'error') {

                alert(`ERROR:\n${data.message}`);
            } else {
                alert('Movement has been insert');
            }
            window.location.href = '/';
        }
        )
        .catch(
            () => console.error('4. ERROR!', "Couldn't access to API")
        );
    console.log('5. Petition made')
}