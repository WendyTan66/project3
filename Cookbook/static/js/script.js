document.addEventListener('DOMContentLoaded', function() {
    //sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });

  //select initialization
  let selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);

  //collapsibles
  let collapsibles = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsibles);






      