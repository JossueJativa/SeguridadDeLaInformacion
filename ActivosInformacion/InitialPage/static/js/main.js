// Función para alternar la visibilidad del contenido
function toggleDropdown() {
  var dropdownContent = document.getElementById("dropdownContent");
  dropdownContent.style.display = (dropdownContent.style.display === "none" || dropdownContent.style.display === "") ? "flex" : "none";
}

function toggleCampoAdicional() {
  var campoAdicional = document.getElementById('campoAdicional');

  // Si el toggle está activado, muestra el campo adicional; de lo contrario, ocúltalo.
  campoAdicional.style.display = document.getElementById('state').checked ? 'block' : 'none';
}

function toggleCampoAdicional2() {
  var campoAdicional = document.getElementById('campoAdicional2');

  // Si el toggle está activado, muestra el campo adicional; de lo contrario, ocúltalo.
  campoAdicional.style.display = document.getElementById('state2').checked ? 'block' : 'none';
}

function actualizarCampos() {
  var valorAsignado = document.getElementById('valorationAssing').value;
  var campoCualitativo = document.getElementById('cualitative');
  var campoDescripcion = document.getElementById('descriptionValue');

  // Colocar el valor cualitativo y la descripción según el valor asignado
  switch (valorAsignado) {
      case '0':
          campoCualitativo.value = 'Despreciable';
          campoDescripcion.value = 'Irrelebante a efectos prácticos';
          break;
      case '1':
          campoCualitativo.value = 'Bajo';
          campoDescripcion.value = 'Daño menor';
          break;
      case '2':
          campoCualitativo.value = 'Bajo';
          campoDescripcion.value = 'Daño menor';
          break;
      case '3':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '4':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '5':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '6':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '7':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '8':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '9':
          campoCualitativo.value = 'Muy Alto';
          campoDescripcion.value = 'Daño muy grave';
          break;
      case '10':
          campoCualitativo.value = 'Extremo';
          campoDescripcion.value = 'Daño extremadamente grave';
          break;
      default:
          campoCualitativo.value = '';
          campoDescripcion.value = '';
  }
}

function actualizarCampos2(){
  var valorAsignado = document.getElementById('valorationAssing2').value;
  var campoCualitativo = document.getElementById('cualitative2');
  var campoDescripcion = document.getElementById('descriptionValue2');

  // Colocar el valor cualitativo y la descripción según el valor asignado
  switch (valorAsignado) {
      case '0':
          campoCualitativo.value = 'Despreciable';
          campoDescripcion.value = 'Irrelebante a efectos prácticos';
          break;
      case '1':
          campoCualitativo.value = 'Bajo';
          campoDescripcion.value = 'Daño menor';
          break;
      case '2':
          campoCualitativo.value = 'Bajo';
          campoDescripcion.value = 'Daño menor';
          break;
      case '3':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '4':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '5':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '6':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '7':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '8':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '9':
          campoCualitativo.value = 'Muy Alto';
          campoDescripcion.value = 'Daño muy grave';
          break;
      case '10':
          campoCualitativo.value = 'Extremo';
          campoDescripcion.value = 'Daño extremadamente grave';
          break;
      default:
          campoCualitativo.value = '';
          campoDescripcion.value = '';
  }
}

function actualizarCampos3(){
  var valorAsignado = document.getElementById('valorationAssing3').value;
  var campoCualitativo = document.getElementById('cualitative3');
  var campoDescripcion = document.getElementById('descriptionValue3');

  switch (valorAsignado) {
      case '0':
          campoCualitativo.value = 'Despreciable';
          campoDescripcion.value = 'Irrelebante a efectos prácticos';
          break;
      case '1':
          campoCualitativo.value = 'Bajo';
          campoDescripcion.value = 'Daño menor';
          break;
      case '2':
          campoCualitativo.value = 'Bajo';
          campoDescripcion.value = 'Daño menor';
          break;
      case '3':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '4':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '5':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '6':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '7':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '8':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '9':
          campoCualitativo.value = 'Muy Alto';
          campoDescripcion.value = 'Daño muy grave';
          break;
      case '10':
          campoCualitativo.value = 'Extremo';
          campoDescripcion.value = 'Daño extremadamente grave';
          break;
      default:
          campoCualitativo.value = '';
          campoDescripcion.value = '';
  }
}

function actualizarCampos4(){
  var valorAsignado = document.getElementById('valorationAssing4').value;
  var campoCualitativo = document.getElementById('cualitative4');
  var campoDescripcion = document.getElementById('descriptionValue4');
  
  switch (valorAsignado) {
      case '0':
          campoCualitativo.value = 'Despreciable';
          campoDescripcion.value = 'Irrelebante a efectos prácticos';
          break;
      case '1':
          campoCualitativo.value = 'Bajo';
          campoDescripcion.value = 'Daño menor';
          break;
      case '2':
          campoCualitativo.value = 'Bajo';
          campoDescripcion.value = 'Daño menor';
          break;
      case '3':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '4':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '5':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '6':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '7':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '8':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '9':
          campoCualitativo.value = 'Muy Alto';
          campoDescripcion.value = 'Daño muy grave';
          break;
      case '10':
          campoCualitativo.value = 'Extremo';
          campoDescripcion.value = 'Daño extremadamente grave';
          break;
      default:
          campoCualitativo.value = '';
          campoDescripcion.value = '';
  }
}

function actualizarCampos5(){
  var valorAsignado = document.getElementById('valorationAssing5').value;
  var campoCualitativo = document.getElementById('cualitative5');
  var campoDescripcion = document.getElementById('descriptionValue5');
  
  switch (valorAsignado) {
      case '0':
          campoCualitativo.value = 'Despreciable';
          campoDescripcion.value = 'Irrelebante a efectos prácticos';
          break;
      case '1':
          campoCualitativo.value = 'Bajo';
          campoDescripcion.value = 'Daño menor';
          break;
      case '2':
          campoCualitativo.value = 'Bajo';
          campoDescripcion.value = 'Daño menor';
          break;
      case '3':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '4':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '5':
          campoCualitativo.value = 'Medio';
          campoDescripcion.value = 'Daño importante';
          break;
      case '6':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '7':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '8':
          campoCualitativo.value = 'Alto';
          campoDescripcion.value = 'Daño grave';
          break;
      case '9':
          campoCualitativo.value = 'Muy Alto';
          campoDescripcion.value = 'Daño muy grave';
          break;
      case '10':
          campoCualitativo.value = 'Extremo';
          campoDescripcion.value = 'Daño extremadamente grave';
          break;
      default:
          campoCualitativo.value = '';
          campoDescripcion.value = '';
  }
}

function agregarValoracion() {
  var addnewvaloration = document.getElementById('text-add-value');
  var hidden_valorationadd1 = document.getElementById('hidden-valorationadd1');

  addnewvaloration.style.display = 'none';
  hidden_valorationadd1.style.display = 'block';
}

function minusValueValoration(){
  var addnewvaloration = document.getElementById('text-add-value');
  var hidden_valorationadd1 = document.getElementById('hidden-valorationadd1');

  addnewvaloration.style.display = 'block';
  hidden_valorationadd1.style.display = 'none';
}

function agregarValoracion2() {
  var addnewvaloration = document.getElementById('text-add-value2');
  var hidden_valorationadd1 = document.getElementById('hidden-valorationadd2');

  addnewvaloration.style.display = 'none';
  hidden_valorationadd1.style.display = 'block';
}

function minusValueValoration2(){
  var addnewvaloration = document.getElementById('text-add-value2');
  var hidden_valorationadd1 = document.getElementById('hidden-valorationadd2');

  addnewvaloration.style.display = 'block';
  hidden_valorationadd1.style.display = 'none';
}

function agregarValoracion3() {
  var addnewvaloration = document.getElementById('text-add-value3');
  var hidden_valorationadd1 = document.getElementById('hidden-valorationadd3');

  addnewvaloration.style.display = 'none';
  hidden_valorationadd1.style.display = 'block';
}

function minusValueValoration3(){
  var addnewvaloration = document.getElementById('text-add-value3');
  var hidden_valorationadd1 = document.getElementById('hidden-valorationadd3');

  addnewvaloration.style.display = 'block';
  hidden_valorationadd1.style.display = 'none';
}

function agregarValoracion4() {
  var addnewvaloration = document.getElementById('text-add-value4');
  var hidden_valorationadd1 = document.getElementById('hidden-valorationadd4');

  addnewvaloration.style.display = 'none';
  hidden_valorationadd1.style.display = 'block';
}

function minusValueValoration4(){
  var addnewvaloration = document.getElementById('text-add-value4');
  var hidden_valorationadd1 = document.getElementById('hidden-valorationadd4');

  addnewvaloration.style.display = 'block';
  hidden_valorationadd1.style.display = 'none';
}

function activeeditbox(button) {
  var departmentId = button.getAttribute('data-department-id');
  var departmentName = button.getAttribute('data-department-name');
  var departmentDescription = button.getAttribute('data-department-description');
  var departmentWorkload = button.getAttribute('data-department-workload');

  // Llenar el formulario en edit-campus con los valores capturados
  document.getElementById('edit-campus').innerHTML = `
    <div class="title">Editar activo</div>
    <input type="hidden" name="departmentId" id="departmentId" value="${departmentId}">
      
      <div class="input-form">
          <label for="departmentName">Nombre de departamento</label><br>
          <input class="input-information" type="text" id="departmentName" name="departmentName" value="${departmentName}">
      </div>

      <div class="input-form">
          <label for="description">Descripción</label><br>
          <input class="input-information" type="text" id="description" name="description" value="${departmentDescription}">
      </div>
      
      <div class="input-form">
          <label for="workload">Cargo</label><br>
          <select name="workload" id="workload" class="input-information"></select>
      </div>
      
      <div class="buttons-end">
          <input type="button" class="buttoncancel" value="Cerrar" onclick="desactiveeditbox()">
          <button type="submit" class="buttonsave">Editar información</button>
      </div>
  `;

  // Hacer una solicitud fetch para obtener la lista de departamentos
  fetch('/home/get-workloads/')
      .then(response => response.json())
      .then(data => {
          // Obtener el elemento del select
          var selectElement = document.getElementById('workload');

          // Iterar sobre los datos y agregar opciones al select
          data.forEach(department => {
              var optionElement = document.createElement('option');
              optionElement.value = department.id;
              optionElement.textContent = department.name;

              // Verificar si el nombre del departamento coincide y seleccionarlo
              if (department.name === departmentWorkload) {
                  optionElement.selected = true;
              }

              selectElement.appendChild(optionElement);
          });
      })
      .catch(error => console.error('Error al obtener la lista de departamentos:', error));

  document.getElementById('overlay').style.display = 'block';
  document.getElementById('edit-campus').style.display = 'block';
}

function activeeditboxUser(button) {
  var userId = button.getAttribute('data-user-id');
  var userId = button.getAttribute('data-user-id');
  var userFirstName = button.getAttribute('data-user-first_name');
  var userLastName = button.getAttribute('data-user-last_name');
  var userUsername = button.getAttribute('data-user-username');
  var userEmail = button.getAttribute('data-user-email');
  var userCelular = button.getAttribute('data-user-celular');
  var userWorkload = button.getAttribute('data-user-workload');
  var userDepartment = button.getAttribute('data-user-department');

  document.getElementById('edit-campus').innerHTML = `
      <div class="title">Editar usuario</div>
      <input type="hidden" name="userId" value="${userId}">
          
      <div class="input-form">
          <label for="userFirstName">Nombre</label><br>
          <input class="input-information" type="text" id="userFirstName" name="userFirstName" value="${userFirstName}">
      </div>

      <div class="input-form">
          <label for="userLastName">Apellido</label><br>
          <input class="input-information" type="text" id="userLastName" name="userLastName" value="${userLastName}">
      </div>

      <div class="input-form">
          <label for="userUsername">Username</label><br>
          <input class="input-information" type="text" id="userUsername" name="userUsername" value="${userUsername}">
      </div>

      <div class="input-form">
          <label for="userEmail">Email</label><br>
          <input class="input-information" type="text" id="userEmail" name="userEmail" value="${userEmail}">
      </div>

      <div class="input-form">
          <label for="userCelular">Celular</label><br>
          <input class="input-information" type="text" id="userCelular" name="userCelular" value="${userCelular}">
      </div>

      <div class="input-form">
          <label for="userDepartment">Departamento</label><br>
          <select name="userDepartment" id="userDepartment" class="input-information"></select>
      </div>

      <div class="input-form">
          <label for="userWorkload">Cargo</label><br>
          <select name="userWorkload" id="userWorkload" class="input-information"></select>
      </div>
      
      <div class="buttons-end">
          <input type="button" class="buttoncancel" value="Cerrar" onclick="desactiveeditboxUser()">
          <button type="submit" class="buttonsave">Editar información</button>
      </div>
  `;

  fetch('/home/get-workloads/')
      .then(response => response.json())
      .then(data => {
          var selectElement = document.getElementById('userWorkload');

          data.forEach(workload => {
              var optionElement = document.createElement('option');
              optionElement.value = workload.id;
              optionElement.textContent = workload.name;

              if (workload.name === userWorkload) {
                  optionElement.selected = true;
              }

              selectElement.appendChild(optionElement);
          });
      })
      .catch(error => console.error('Error al obtener la lista de cargos:', error));

  fetch('/home/get-departments/')
      .then(response => response.json())
      .then(data => {
          var selectElement = document.getElementById('userDepartment');

          data.forEach(department => {
              var optionElement = document.createElement('option');
              optionElement.value = department.id;
              optionElement.textContent = department.name;

              if (department.name === userDepartment) {
                  optionElement.selected = true;
              }

              selectElement.appendChild(optionElement);
          });
      })
      .catch(error => console.error('Error al obtener la lista de cargos:', error));

  document.getElementById('overlay').style.display = 'block';
  document.getElementById('edit-campus').style.display = 'block';
}

function desactiveeditboxUser() {
  document.getElementById('overlay').style.display = 'none';
  document.getElementById('edit-campus').style.display = 'none';
}

function activeeditboxAsset(button) {
  var assetValueID = button.getAttribute('data-assetValue-id');
  var assetId = button.getAttribute('data-asset-id');
  var assetCode = button.getAttribute('data-asset-code');
  var assetName = button.getAttribute('data-asset-name');
  var assetOrigin = button.getAttribute('data-asset-origin');
  var assetUbicationType = button.getAttribute('data-asset-ubicationType');
  var assetUbication = button.getAttribute('data-asset-ubication');
  var assetQuantity = button.getAttribute('data-asset-quantity');
  var assetCharacteristic = button.getAttribute('data-asset-characteristic');
  var assetType = button.getAttribute('data-asset-type');
  var assetSubtype = button.getAttribute('data-asset-subtype');
  var assetResponsableArea = button.getAttribute('data-asset-responsableArea');
  var assetResponsableUser = button.getAttribute('data-asset-responsableUser');
  var assetDimentionValue = button.getAttribute('data-asset-dimentionValue');
  var assetCuantityValue = button.getAttribute('data-asset-cuantityValue');
  var assetCualityValue = button.getAttribute('data-asset-cualityValue');
  var assetDescription = button.getAttribute('data-asset-description');

  document.getElementById('edit-campus').innerHTML = `
      <div class="title">Editar activo</div>
      <input type="hidden" name="assetId" value="${assetId}">
      <input type="hidden" name="assetValueID" value="${assetValueID}">
          
      <div class="input-form">
        <label for="origin">Origen</label><br>
        <input class="input-information" type="text" id="origin" name="origin" value="${assetOrigin}">
      </div>

      <div class="input-form">
          <label for="code">Código</label><br>
          <input class="input-information" type="text" id="code" name="code" value="${assetCode}">
      </div>

      <div class="input-form">
          <label for="name">Nombre</label><br>
          <input class="input-information" type="text" id="name" name="name" value="${assetName}">
      </div>

      <div class="input-form">
        <label for="type">Tipo</label><br>
        <select name="type" id="type" class="input-information" onchange="populateSubtypesEdit(this.value)">
        </select>
      </div>

      <div class="input-form">
        <label for="subtype">Subtipo</label><br>
        <select name="subtype" id="subtype" class="input-information">
        </select>
      </div>

      <div class="input-form">
      <label for="responsableArea">Area responsable</label><br>
        <select name="responsableArea" id="responsableArea" class="input-information">
        </select>
      </div>

      <div class="input-form">
          <label for="responsablePerson">Persona responsable
          </label><br>
          <select name="responsablePerson" id="responsablePerson" class="input-information">
          </select>
      </div>

      <div class="input-form">
        <label for="ubicationType">Tipo de ubicación</label><br>
        <select name="ubicationType" id="ubicationType" class="input-information">
        </select>
      </div>

      <div class="input-form">
        <label for="ubication">Ubicación</label><br>
        <input class="input-information" type="text" id="ubication" name="ubication" value="${assetUbication}">
      </div>

      <div class="input-form">
          <label for="quantity">Cantidad</label><br>
          <input class="input-information" type="number" id="quantity" name="quantity" value="${assetQuantity}">
      </div>
  
      <div class="input-form">
          <label for="characteristic">Caracteristica</label><br>
          <input class="input-information" type="text" id="characteristic" name="characteristic" value="${assetCharacteristic}">
      </div>

      <div class="toggle-text">
          <label for="state2">¿Deseas valorar el activo?</label><br>
          <label class="switch">
              <input type="checkbox" id="state2" name="state2" class="offset" onchange="toggleCampoAdicional2()">
              <span class="slider"></span>
          </label>
      </div>

      <div id="campoAdicional2" class="hidden">
        <div class="underline-text">Valoración</div>

        <div class="input-form">
            <label for="valorationDimention">Dimensión de valoracion</label><br>
            <select name="valorationDimention" id="valorationDimention" class="input-information">
                <option value="">Selecciona la dimensión</option>
                <option value="" disabled>-------------------------------------------------------------------------------------------------</option>
                <option value="Disponibilidad">Disponibilidad</option>
                <option value="Integridad">Integridad</option>
                <option value="Confidencialidad">Confidencialidad</option>
                <option value="Autenticidad">Autenticidad</option>
                <option value="Trazabilidad">Trazabilidad</option>
            </select>
        </div>

        <div class="input-form">
            <label for="valorationAssing">Valor asignado (0-10)</label><br>
            <select name="valorationAssing" id="valorationAssing" class="input-information" onchange="actualizarCampos()">
                <option value="">Seleccione el valor</option>
                <option value="" disabled>-------------------------------------------------------------------------------------------------</option>
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
            </select>
        </div>

        <div class="input-form">
            <label for="cualitative">Valor cualitativo</label><br>
            <input class="input-information" type="text" id="cualitative" name="cualitative" value="${assetCualityValue}" style="opacity: 50%; cursor: default;" readonly>
        </div>
    
        <div class="input-form">
            <label for="descriptionValue">Descripción</label><br>
            <input class="input-information" type="text" id="descriptionValue" name="descriptionValue" value="${assetDescription}" style="opacity: 50%; cursor: default;" readonly>
        </div>
      </div>

      <div class="buttons-end">
          <input type="button" class="buttoncancel" value="Cerrar" onclick="desactiveeditboxAsset()">
          <button type="submit" class="buttonsave">Editar información</button>
      </div>
  `;

  var selectUbicationType = document.getElementById('ubicationType');
  var ubicationTypeOptions = ['Técnica', 'Geográfica'];

  // Seleccionar la dimensión y el valor asignado según los valores recuperados
  var selectDimention = document.getElementById('valorationDimention');
  selectDimention.value = assetDimentionValue;

  var selectValue = document.getElementById('valorationAssing');
  selectValue.value = assetCuantityValue;

  ubicationTypeOptions.forEach(optionValue => {
      var optionElement = document.createElement('option');
      optionElement.value = optionValue;
      optionElement.textContent = optionValue;

      // Verificar si la opción coincide con assetUbicationType
      if (optionValue === assetUbicationType) {
          optionElement.selected = true;
      }

      selectUbicationType.appendChild(optionElement);
  });

  // Aquí puedes agregar el código para llenar los campos del formulario según los valores recuperados
  fetch('/home/get-types/')
      .then(response => response.json())
      .then(data => {
          // Obtener el elemento del select
          var selectElement = document.getElementById('type');

          // Iterar sobre los datos y agregar opciones al select
          data.forEach(type => {
              var idtype = type.id
              var optionElement = document.createElement('option');
              optionElement.value = type.id;
              optionElement.textContent = type.name;

              // Verificar si el nombre del departamento coincide y seleccionarlo
              if (type.name === assetType) {
                  optionElement.selected = true;
              }

              selectElement.appendChild(optionElement);
          });
      })
      .catch(error => console.error('Error al obtener la lista de departamentos:', error));

  fetch(`/home/get-subtypes2/`)
      .then(response => response.json())
      .then(data => {
          // Obtener el elemento del select
          var selectElement = document.getElementById('subtype');
          // Iterar sobre los datos y agregar opciones al select
          data.forEach(subtype => {
              var optionElement = document.createElement('option');
              optionElement.value = subtype.id;
              optionElement.textContent = subtype.name;
              // Verificar si el nombre del departamento coincide y seleccionarlo
              if (subtype.name === assetSubtype) {
                  optionElement.selected = true;
              }
              selectElement.appendChild(optionElement);
          });
      })
      .catch(error => console.error('Error al obtener la lista de departamentos:', error));

      fetch(`/home/get-departments/`)
      .then(response => response.json())
      .then(data => {
          // Obtener el elemento del select
          var selectElement = document.getElementById('responsableArea');
          // Iterar sobre los datos y agregar opciones al select
          data.forEach(departments => {
              var optionElement = document.createElement('option');
              optionElement.value = departments.id;
              optionElement.textContent = departments.name;
              // Verificar si el nombre del departamento coincide y seleccionarlo
              if (departments.name === assetResponsableArea) {
                  optionElement.selected = true;
              }
              selectElement.appendChild(optionElement);
          });
      })
      .catch(error => console.error('Error al obtener la lista de departamentos:', error));

      fetch(`/home/get-users/`)
      .then(response => response.json())
      .then(data => {
          // Obtener el elemento del select
          var selectElement = document.getElementById('responsablePerson');
          // Iterar sobre los datos y agregar opciones al select
          data.forEach(users => {
              var optionElement = document.createElement('option');
              optionElement.value = users.id;
              optionElement.textContent = `${users.first_name} ${users.last_name}`;
              // Verificar si el nombre del departamento coincide y seleccionarlo
              if (`${users.first_name} ${users.last_name}` === assetResponsableUser) {
                  optionElement.selected = true;
              }
              selectElement.appendChild(optionElement);
          });
      })
      .catch(error => console.error('Error al obtener la lista de departamentos:', error));


  var selectTypeElement = document.getElementById('type');
  // Agregar un evento de cambio para llamar a populateSubtypesEdit
  selectTypeElement.addEventListener('change', function() {
    var selectedType = selectTypeElement.value;
    populateSubtypesEdit(selectedType);
  });

  document.getElementById('overlay').style.display = 'block';
  document.getElementById('edit-campus').style.display = 'block';
}

function desactiveeditboxAsset() {
  document.getElementById('overlay').style.display = 'none';
  document.getElementById('edit-campus').style.display = 'none';
}

// Nueva función para cargar los subtipos según el tipo seleccionado
function populateSubtypesEdit(selectedType) {
  const subtypeDropdown = document.getElementById('subtype');

  // Make an AJAX request
  fetch(`/home/get-subtypes/${selectedType}/`)
    .then(response => response.json())
    .then(data => {
      // Clear previous options
      subtypeDropdown.innerHTML = '';

      // Add new options
      data.forEach(subtype => {
        const option = document.createElement('option');
        option.value = subtype.id;
        option.textContent = subtype.name;
        subtypeDropdown.appendChild(option);
      });
    })
    .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function () {
  function populateSubtypes() {
      const assetTypeDropdown = document.getElementById('type');
      const subtypeDropdown = document.getElementById('subtype');
      const assetTypeId = assetTypeDropdown.value;

      // Make an AJAX request
      fetch(`/home/get-subtypes/${assetTypeId}/`)
          .then(response => response.json())
          .then(data => {
              // Clear previous options
              subtypeDropdown.innerHTML = '';

              // Add new options
              data.forEach(subtype => {
                  const option = document.createElement('option');
                  option.value = subtype.id;
                  option.textContent = subtype.name;
                  subtypeDropdown.appendChild(option);
              });
          })
          .catch(error => console.error('Error:', error));
  }

  // Trigger the initial population
  populateSubtypes();

  // Trigger the population when the asset type changes
  const assetTypeDropdown = document.getElementById('type');
  assetTypeDropdown.addEventListener('change', populateSubtypes);

  // Trigger the population when the modal is shown
  const editModals = document.querySelectorAll('.edit-modal');
  editModals.forEach(modal => {
      modal.addEventListener('shown.bs.modal', populateSubtypes);
  });
});

function desactiveeditbox(){
  document.getElementById('overlay').style.display = 'none';
  document.getElementById('edit-campus').style.display = 'none';
}

function activeeditboxRisk(button) {
  var riskID = button.getAttribute('data-risk-id');
  var riskAssetId = button.getAttribute('data-risk-asset-id');
  var riskAssetTypeId = button.getAttribute('data-risk-asset-type-id');
  var riskAssetName = button.getAttribute('data-risk-asset-name');
  var riskDimention = button.getAttribute('data-risk-dimention');
  var riskTypeId = button.getAttribute('data-risk-type-id');

  idToFilter = Number(riskAssetTypeId);

  var subRisksIds = [];
  var subRiskIdElements = document.querySelectorAll('[data-subrisk-id]');
  subRiskIdElements.forEach(function(element) {
      subRisksIds.push(element.getAttribute('data-subrisk-id'));
  });

  document.getElementById('edit-campus').innerHTML = `
      <div class="title">Editar riesgo</div>
      <input type="hidden" name="riskId" value="${riskID}">
      <input type="hidden" name="asset" value="${riskAssetId}">

      <div class="input-form">
        <label for="">Activo</label><br>
        <input class="input-information" type="text" id="" name="" value="${riskAssetName}" readonly>
      </div>
      
      <div class="input-form">
        <label for="impact">Impacto</label><br>
        <select name="impact" id="impact" class="input-information">
          <option value="">Selecciona un impacto</option>
          <option value="">--------------------------------------------------------------------------------------------------</option>
          <option value="MA">Muy Alta</option>
          <option value="A">Alta</option>
          <option value="M">Media</option>
          <option value="B">Baja</option>
          <option value="MB">Muy Baja</option>
        </select>
      </div>

      <div class="input-form">
        <label for="probability">Probabilidad</label><br>
        <select name="probability" id="probability" class="input-information">
          <option value="">Selecciona una probabilidad</option>
          <option value="">--------------------------------------------------------------------------------------------------</option>
          <option value="MA">Muy Alta</option>
          <option value="A">Alta</option>
          <option value="M">Media</option>
          <option value="B">Baja</option>
          <option value="MB">Muy Baja</option>
        </select>
      </div>

      <div class="input-form">
        <label for="">Riesgo</label><br>
        <input class="input-information" type="text" id="" name="" value="${riskDimention}" readonly>
      </div>

      <img src="../../static/img/Estimacion Del Riesgo.jpg" alt="Riesgo" style="width: 50%; height: 50%; transform: translate(50%, 0%);">

      <div class="input-form">
        <label for="risk">Tipos de riesgos</label><br>
        <select name="risk" id="risk" class="input-information" onchange="getRisk(this.value)">
          <option value="0">Selecciona un tipo de riesgo</option>
          <option value="0">--------------------------------------------------------------------------------------------------</option>
        </select>
      </div>

      <div class="input-form">
        <label for="addrisk">Riesgos</label><br>
        <br>
        <div id="addrisk"></div>
      </div>

      <br>

      <div class="buttons-end">
        <input type="button" class="buttoncancel" value="Cerrar" onclick="desactiveeditboxRisk()">
        <button type="submit" class="buttonsave">Editar información</button>
      </div>
  `;

  fetch(`/home/get-risktypes/`)
      .then(response => response.json())
      .then(data => {
        const container = document.getElementById("risk");
        container.innerHTML = "";

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
                        if(riskTypeId == data[i].id){
                          option.selected = true;
                        }
                    }
                    break;
                case 11:
                    if (data[i].id === 4){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                        if(riskTypeId == data[i].id){
                          option.selected = true;
                        }
                    }
                    break;
                case 10:
                    if (data[i].id === 2){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                        if(riskTypeId == data[i].id){
                          option.selected = true;
                        }
                    }
                    break;
                case 9:
                    if (data[i].id === 2){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                        if(riskTypeId == data[i].id){
                          option.selected = true;
                        }
                    }
                    break;
                case 8:
                    if (data[i].id === 2 || data[i].id === 4){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                        if(riskTypeId == data[i].id){
                          option.selected = true;
                        }
                    }
                    break;
                case 6:
                    if (data[i].id === 2 || data[i].id === 4 || data[i].id === 3){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                        if(riskTypeId == data[i].id){
                          option.selected = true;
                        }
                    }
                    break;
                case 5:
                    if (data[i].id === 4 || data[i].id === 3){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                        if(riskTypeId == data[i].id){
                          option.selected = true;
                        }
                    }
                    break;
                case 4:
                    if (data[i].id === 4 || data[i].id === 3){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                        if(riskTypeId == data[i].id){
                          option.selected = true;
                        }
                    }
                    break;
                case 3:
                    if (data[i].id === 4 || data[i].id === 3){
                        const option = document.createElement('option');
                        option.value = data[i].id;
                        option.appendChild(document.createTextNode(data[i].name));
                        container.appendChild(option);
                        if(riskTypeId == data[i].id){
                          option.selected = true;
                        }
                    }
                    break;
                default:
                    const option = document.createElement('option');
                    option.value = data[i].id;
                    option.appendChild(document.createTextNode(data[i].name));
                    container.appendChild(option);
                    if(riskTypeId == data[i].id){
                      option.selected = true;
                    }
                    break;
            }
        }
      })

  fetch(`/home/get-risks/${riskTypeId}`)
      .then(response => response.json())
      .then(data => {
        const container = document.getElementById("addrisk");
        container.innerHTML = "";
        valueToFilter = Number(idToFilter);

        for (let i = 0; i < data.length; i++) {
          const checkbox = document.createElement('input');
          checkbox.type = 'checkbox';
          checkbox.name = 'selectedRisks';
          checkbox.value = data[i].id;
          checkbox.id = `risk${data[i].id}`;

          // Verificar si el ID está en subRisksIds
          const isIdInSubRisks = subRisksIds.includes(data[i].id.toString());

          // Marcar el checkbox si el ID está en subRisksIds
          if (isIdInSubRisks) {
            checkbox.checked = true;
          }else{
            checkbox.disabled = true;
          }
          

          const label = document.createElement('label');
          label.htmlFor = `risk${data[i].id}`;
          label.appendChild(document.createTextNode(data[i].name));

          container.appendChild(checkbox);
          container.appendChild(label);
          container.appendChild(document.createElement('br'));

          // Desactivar checkboxes no seleccionados
          if (!checkbox.checked) {
            checkbox.disabled = true;
          }
        }
      })

  document.getElementById('overlay').style.display = 'block';
  document.getElementById('edit-campus').style.display = 'block';
}

function desactiveeditboxRisk() {
  document.getElementById('overlay').style.display = 'none';
  document.getElementById('edit-campus').style.display = 'none';
}

function activeeditboxSafeguard(button){
  var safeguardID = button.getAttribute('data-safeguard-id');
  var safeguardName = button.getAttribute('data-safeguard-name');
  var safeguardAssetId = button.getAttribute('data-safeguard-asset-id');
  var safeguardAssetName = button.getAttribute('data-safeguard-asset-name');
  var safeguardSafeguardTypeId = button.getAttribute('data-safeguard-safeguard-type-id');
  var safeguardSafeguardTypeName = button.getAttribute('data-safeguard-safeguard-type-name');

  var safeguars = [];
  var safeguarElements = document.querySelectorAll('[data-safeguard-options-id]');
  safeguarElements.forEach(function(element) {
      safeguars.push(element.getAttribute('data-safeguard-options-id'));
  });

  document.getElementById('edit-campus').innerHTML = `
      <div class="title">Editar salvaguarda</div>
      <input type="hidden" name="safeguardId" value="${safeguardID}">
      <input type="hidden" name="asset" value="${safeguardAssetId}">

      <div class="input-form">
        <label for="">Activo</label><br>
        <input class="input-information" type="text" id="" name="" value="${safeguardAssetName}" readonly>
      </div>

      <div class="input-form">
        <label for="safeguard">Salvaguarda</label><br>
        <input class="input-information" type="text" id="" name="" value="${safeguardSafeguardTypeName}" readonly>
      </div>

      <div class="buttons-end">
        <input type="button" class="buttoncancel" value="Cerrar" onclick="desactiveeditboxSafeguard()">
        <button type="submit" class="buttonsave">Editar información</button>
      </div>
      `

      document.getElementById('overlay').style.display = 'block';
      document.getElementById('edit-campus').style.display = 'block';
}

function desactiveeditboxSafeguard() {
  document.getElementById('overlay').style.display = 'none';
  document.getElementById('edit-campus').style.display = 'none';
}

try{
  document.getElementById("inpSearch0").addEventListener("input", e => {
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[0];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
}catch{

}

try{
  document.getElementById("inpSearch1").addEventListener("input", e => {
    console.log(e.target.value);
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[1];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
} catch {

}


try{
  document.getElementById("inpSearch2").addEventListener("input", e => {
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[2];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
}catch{

}

try{
  document.getElementById("inpSearch3").addEventListener("input", e => {
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[3];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
}catch {

}

try{
  document.getElementById("inpSearch4").addEventListener("input", e => {
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[4];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
} catch{

}

try{
  document.getElementById("inpSearch5").addEventListener("input", e => {
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[5];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
}catch{

}

try{
  document.getElementById("inpSearch7").addEventListener("input", e => {
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[7];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
}catch{

}

try{
  document.getElementById("inpSearch8").addEventListener("input", e => {
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[8];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
}catch{

}

try{
  document.getElementById("inpSearch9").addEventListener("input", e => {
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[9];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
}catch{

}

try{
  document.getElementById("inpSearch12").addEventListener("input", e => {
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[12];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
}catch{

}

try{
  document.getElementById("inpSearch13").addEventListener("input", e => {
    const searchInput = e.target.value.toLowerCase();
    const tabla = document.getElementById("searchtable");
    const tr = tabla.getElementsByTagName("tr");
  
    for (let i = 1; i < tr.length; i++) {
      const td = tr[i].getElementsByTagName("td")[13];
  
      if (td) {
        const txtValue = td.textContent || td.innerText;
        const txtValueLowerCase = txtValue.toLowerCase();
  
        if (txtValueLowerCase.includes(searchInput)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  });
}catch{

}

function getRisk(risk) {
  valueToFilter = sessionStorage.getItem("idToFilter");
  try {
      fetch(`/home/get-risks/${risk}`, {
          method: 'GET',
      })
          .then(response => response.json())
          .then(data => {
              console.log(data);
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

                  // Desactivar checkboxes no seleccionados
                  if (!checkbox.checked) {
                    checkbox.disabled = true;
                  }
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
  fetch(`/home/get-risktypes`)
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

function getSafeguardsOptions(idToFilter){
  idToFilter = Number(idToFilter);
  fetch(`/home/get-safeguardstypes/`)
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById("safeguard");
    container.innerHTML = ""; // Vaciar el contenedor

    // Agregar las dos opciones por defecto
    let defaultOption = document.createElement('option');
    defaultOption.value = "";
    defaultOption.appendChild(document.createTextNode("Selecciona un salvaguarda"));
    container.appendChild(defaultOption);

    defaultOption = document.createElement('option');
    defaultOption.value = "";
    defaultOption.appendChild(document.createTextNode("------------------------------------------------------------------------------------------------"));
    container.appendChild(defaultOption);

    for (let i = 0; i < data.length; i++) {
      const option = document.createElement('option');
      switch(idToFilter){
        case 1:
          if (data[i].id === 0){
            option.value = 0;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;
  
        case 2:
          if (data[i].id === 1){
            option.value = 1;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;
  
        case 3:
          if (data[i].id === 2){
            option.value = 2;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;

        case 4:
          if (data[i].id === 3){
            option.value = 3;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;

        case 5:
          if (data[i].id === 4){
            option.value = 4;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;

        case 6:
          if (data[i].id === 5){
            option.value = 5;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;

        case 7:
          if (data[i].id === 6){
            option.value = 6;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;

        case 8:
          if (data[i].id === 7){
            option.value = 7;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;

        case 9:
          if (data[i].id === 8){
            option.value = 8;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;

        case 10:
          if (data[i].id === 9){
            option.value = 9;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;

        case 11:
          if (data[i].id === 10){
            option.value = 10;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;

        case 12:
          if (data[i].id === 11){
            option.value = 11;
            option.appendChild(document.createTextNode(data[i].name));
            container.appendChild(option);
          }
          break;

        default:
          option.value = data[i].id;
          option.appendChild(document.createTextNode(data[i].name));
          container.appendChild(option);
          break;
      }
    }
  });
}

function getSafeguardsData(idSafeguard){
  fetch(`/home/get-safeguards/${idSafeguard}`)
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById("addsafeguards");

    container.innerHTML = "";

    for (let i = 0; i < data.length; i++) {
      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.name = 'selectedSafeguards';
      checkbox.value = data[i].id;
      checkbox.id = `safeguard${data[i].id}`;

      const label = document.createElement('label');
      label.htmlFor = `safeguard${data[i].id}`;
      label.appendChild(document.createTextNode(`[${data[i].code}] ${data[i].name}`));

      container.appendChild(checkbox);
      container.appendChild(label);
      container.appendChild(document.createElement('br'));
    }
  }).catch(error => console.error('Error:', error));
}