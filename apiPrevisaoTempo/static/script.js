function getWeather() {
    let city = document.getElementById("city").value;

    if (city === "") {
        alert("Por favor, digite uma cidade!");
        return;
    }

    fetch(`/weather?city=${city}`)
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerHTML = "Erro: " + data.error;
        } else {
            document.getElementById("result").innerHTML = `
                <p><strong>Cidade:</strong> ${data.city}</p>
                <p><strong>Temperatura:</strong> ${data.temperature}°C</p>
                <p><strong>Condição:</strong> ${data.description}</p>
            `;
        }
    })
    .catch(error => {
        document.getElementById("result").innerHTML = "Erro ao buscar dados.";
    });
}
