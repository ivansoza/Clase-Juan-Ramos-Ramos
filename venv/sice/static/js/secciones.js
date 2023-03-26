function search() {
    var query = document.getElementById("search-box").value.toLowerCase();
    var sections = document.querySelectorAll("[data-searchable]");
    var results = [];
  
    for (var i = 0; i < sections.length; i++) {
      var content = sections[i].textContent.toLowerCase();
      if (content.indexOf(query) !== -1) {
        results.push(sections[i]);
      }
    }
  
    // hacer algo con los resultados (por ejemplo, mostrarlos en una lista)
  }
  