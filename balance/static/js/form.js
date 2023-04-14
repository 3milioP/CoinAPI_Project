console.log('--- Iniciamos ejecución de form.js ---');

const APIKEY = 'E6A881EC-A489-4A17-BD9D-354A4625D54A'

const form = document.getElementById('form-mov');
const calculate = document.getElementById('calculate')

form.addEventListener('submit', sendForm);
calculate.addEventListener('click', calculateForm);

function calculateForm() {

    let fromCurrency = document.getElementById("from_currency");
    let origin = fromCurrency.options[fromCurrency.selectedIndex].value;

    let toCurrency = document.getElementById("to_currency");
    let destiny = toCurrency.options[toCurrency.selectedIndex].value;

    let fromQuantity = document.getElementById("from_quantity");
    let qtt = fromQuantity.value;

    if (origin != destiny) {
        fetch(`https://rest.coinapi.io/v1/exchangerate/${origin}/${destiny}`, {
            method: "GET",
            headers: {
                'X-CoinAPI-Key': APIKEY
            }
        })
            .then(response => response.json())
            .then(response => {
                const options = {
                    minimumFractionDigits: 2,
                    maximumFractionDigits: 2
                };
                const formatter = new Intl.NumberFormat('es-ES', options);

                const exRate = response.rate

                let toQuantity = document.getElementById("to_quantity")
                toQuantity.value = formatter.format(exRate * qtt);

                let uPrice = document.getElementById("u_price");
                uPrice.value = formatter.format(exRate)
            })
    } else {
        alert('Currency FROM must be different of currency TO')
    }

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

window.onload = function () {
    purchaseNav = document.getElementById('purchase');
    purchaseNav.style.pointerEvents = "none";
    purchaseNav.style.color = "#999";
}