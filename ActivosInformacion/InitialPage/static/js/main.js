
document.getElementById("inpSearch").addEventListener("input", e => {
    console.log(e.target.value)
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