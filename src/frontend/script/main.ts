const burgerDiv = document.querySelector('.burger');

if (burgerDiv) {
  window.addEventListener('resize', function() {
    if (window.innerWidth > 700) {
      const linksMenu = document.querySelector('.header-content');
      burgerDiv.classList.remove('_active');
      document.body.classList.remove('_lock');
      if (linksMenu) {
        linksMenu.classList.remove('_active');
      }
    }
  })
  burgerDiv.addEventListener('click', function() {
    const linksMenu = document.querySelector('.header-content');
    burgerDiv.classList.toggle('_active');
    if (linksMenu) {
      linksMenu.classList.toggle('_active');
    }
    document.body.classList.toggle('_lock');
  })
}

