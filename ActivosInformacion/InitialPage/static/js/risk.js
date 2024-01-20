function getRisk() {
    try {
        var risk = document.getElementById("risk").value;

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
                checkbox.name = 'selectedRisks';  // Nombre común para todos los checkboxes
                checkbox.value = data[i].id;
                checkbox.id = `risk${data[i].id}`;

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