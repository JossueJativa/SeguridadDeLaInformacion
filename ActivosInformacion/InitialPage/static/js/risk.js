function getRisk(risk) {
    valueToFilter = sessionStorage.getItem("idToFilter");
    try {
        fetch(`http://127.0.0.1:8000/home/get-risks/${risk}`, {
            method: 'GET',
        })
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById("addrisk");
                container.innerHTML = "";
                valueToFilter = Number(valueToFilter); // Convertir a número

                for (let i = 0; i < data.length; i++) {
                    const checkbox = document.createElement('input');
                    checkbox.type = 'checkbox';
                    checkbox.name = 'selectedRisks';
                    checkbox.value = data[i].id;
                    checkbox.id = `risk${data[i].id}`;
                    if (valueToFilter === 12) {
                        if (data[i].id === 20){
                            checkbox.checked = true;
                        }
                    }else if (valueToFilter === 11) {
                        if (data[i].id === 54){
                            checkbox.checked = true;
                        }
                    }else if (valueToFilter === 10) {
                        if (data[i].id === 13){
                            checkbox.checked = true;
                        }
                    }else if (valueToFilter === 9) {
                        if (data[i].id === 14){
                            checkbox.checked = true;
                        }
                    }else if (valueToFilter === 8) {
                        if (data[i].id === 12 || data[i].id === 43 || data[i].id === 45){
                            checkbox.checked = true;
                        }
                    }else if (valueToFilter === 7) {
                        if (data[i].id === 1 || data[i].id === 2 || data[i].id === 3){
                            checkbox.checked = true;
                        }
                        if (data[i].id === 4 || data[i].id === 5 || data[i].id === 6 || data[i].id === 10 || data[i].id === 11 || data[i].id === 15){
                            checkbox.checked = true;
                        }
                        if(data[i].id === 30 || data[i].id === 32){
                            checkbox.checked = true;
                        }
                        if(data[i].id === 52 || data[i].id === 53){
                            checkbox.checked = true;
                        }
                    }else if (valueToFilter === 6) {
                        if (data[i].id === 5){
                            checkbox.checked = true;
                        }
                        if (data[i].id === 28 || data[i].id === 29 || data[i].id === 21){
                            checkbox.checked = true;
                        }
                        if(data[i].id === 39 || data[i].id === 49){
                            checkbox.checked = true;
                        }
                    }
                    else if (valueToFilter === 5) {
                        if (data[i].id === 22 || data[i].id === 23 || data[i].id === 24 || data[i].id === 31){
                            checkbox.checked = true;
                        }
                        if (data[i].id === 38 || data[i].id === 40 || data[i].id === 41 || data[i].id === 44 || data[i].id === 51){
                            checkbox.checked = true;
                        }
                    }else if (valueToFilter === 4) {
                        if (data[i].id === 16 || data[i].id === 17 || data[i].id === 25 || data[i].id === 26 || data[i].id === 27){
                            checkbox.checked = true;
                        }
                        if (data[i].id === 36 || data[i].id === 37 || data[i].id === 42 || data[i].id === 46 || data[i].id === 47 || data[i].id === 48){
                            checkbox.checked = true;
                        }
                    }else if (valueToFilter === 3) {
                        if (data[i].id === 16 || data[i].id === 17 || data[i].id === 25 || data[i].id === 26 || data[i].id === 27){
                            checkbox.checked = true;
                        }
                        if (data[i].id === 36 || data[i].id === 37 || data[i].id === 42 || data[i].id === 46 || data[i].id === 47 || data[i].id === 48){
                            checkbox.checked = true;
                        }
                    }else {
                        checkbox.checked = false;
                    }

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
    idToFilter = Number(idToFilter);
    sessionStorage.setItem("idToFilter", idToFilter);
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