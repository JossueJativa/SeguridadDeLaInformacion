// Función para alternar la visibilidad del contenido
function toggleDropdown() {
  var dropdownContent = document.getElementById("dropdownContent");
  dropdownContent.style.display = (dropdownContent.style.display === "none" || dropdownContent.style.display === "") ? "flex" : "none";
}


document.getElementById("inpSearch").addEventListener("input", e => {
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

  try{
    document.getElementById("inpSearchAsset").addEventListener("input", e => {
      console.log(e.target.value)
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

    document.getElementById("inpSearchDepartment").addEventListener("input", e => {
      console.log(e.target.value)
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
  }
  catch(error){
  }