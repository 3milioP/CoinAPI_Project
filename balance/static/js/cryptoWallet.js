function cryptoWallet() {
    fetch('http://localhost:5000/api/v1/movements/data')
        .then(response => response.json())
        .then(response => {
            const wallet = response.crypto_balance
            let htmlWallet = '';
            for (const crypto in wallet) {
                htmlWallet += `
                  <a class="navbar-item">
                      ${crypto} - ${wallet[crypto]}
                  </a>
                `
            }
            const navWallet = document.getElementById('wallet');
            navWallet.innerHTML += htmlWallet;
        })
        .catch((error) => console.log('ERROR: Error al cargar los datos', error));
}

window.addEventListener('load', cryptoWallet);