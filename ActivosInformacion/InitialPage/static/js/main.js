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