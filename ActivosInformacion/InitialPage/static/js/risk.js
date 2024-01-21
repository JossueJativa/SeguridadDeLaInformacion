function getRisk(risk) {
    try {
        fetch(`http://127.0.0.1:8000/home/get-risks/${risk}`, {
            method: 'GET',
        })
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById("addrisk");
                container.innerHTML = "";

                for (let i = 0; i < data.length; i++) {
                    const checkbox = document.createElement('input');
                    checkbox.type = 'checkbox';
                    checkbox.name = 'selectedRisks';
                    checkbox.value = data[i].id;
                    checkbox.id = `risk${data[i].id}`;
                    checkbox.checked = true; // Añadir esta línea

                    const label = document.createElement('label');
                    label.htmlFor = `risk${data[i].id}`;
                    label.appendChild(document.createTextNode(data[i].name));

                    container.appendChild(checkbox);
                    container.appendChild(label);
                    container.appendChild(document.createElement('br'));
                }
            });
    } catch (error) {
        const container = document.getElementById("addrisk");
        container.innerHTML = "-- Seleccione un riesgo --";
    }
}

function getRiskOptions(idToFilter){
    idToFilter = Number(idToFilter); // Convertir a número
    fetch(`http://127.0.0.1:8000/home/get-risktypes`)
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById("risk");
        container.innerHTML = ""; // Vaciar el contenedor

        // Agregar las dos opciones por defecto
        let defaultOption = document.createElement('option');
        defaultOption.value = "";
        defaultOption.appendChild(document.createTextNode("Selecciona un activo"));
        container.appendChild(defaultOption);

        defaultOption = document.createElement('option');
        defaultOption.value = "";
        defaultOption.appendChild(document.createTextNode("------------------------------------------------------------------------------------------------"));
        container.appendChild(defaultOption);

        for (let i = 0; i < data.length; i++) {
            switch (idToFilter) {
                case 12:
                    if (data[i].id === 3){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                    }
                    break;
                case 11:
                    if (data[i].id === 4){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                    }
                    break;
                case 10:
                    if (data[i].id === 2){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                    }
                    break;
                case 9:
                    if (data[i].id === 2){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                    }
                    break;
                case 8:
                    if (data[i].id === 2 || data[i].id === 4){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                    }
                    break;
                case 6:
                    if (data[i].id === 2 || data[i].id === 4 || data[i].id === 3){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                    }
                    break;
                case 5:
                    if (data[i].id === 4 || data[i].id === 3){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                    }
                    break;
                case 4:
                    if (data[i].id === 4 || data[i].id === 3){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                    }
                    break;
                case 3:
                    if (data[i].id === 4 || data[i].id === 3){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                    }
                    break;
                default:
                    const option = document.createElement('option');
                    option.value = data[i].id;
                    option.appendChild(document.createTextNode(data[i].name));
                    container.appendChild(option);
                    break;
            }
        }
    });
}