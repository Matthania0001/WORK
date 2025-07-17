document.addEventListener('DOMContentLoaded', function() {
  // Gestion des clics sur les boutons
  const buttons = document.querySelectorAll('.header button');
  
  buttons.forEach(button => {
    button.addEventListener('click', function() {
      const url = this.getAttribute('data-url');
      if (url) {
        window.location.href = url;
      }
    });
    
    // Effet de survol amélioré
    button.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-2px)';
      this.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
    });
    
    button.addEventListener('mouseleave', function() {
      this.style.transform = '';
      this.style.boxShadow = '';
    });
  });
  
  // Animation au chargement
  setTimeout(() => {
    document.querySelector('.header').style.opacity = '1';
  }, 100);
});

// Ajout d'une classe quand on scroll
window.addEventListener('scroll', function() {
  const header = document.querySelector('.header');
  if (window.scrollY > 50) {
    header.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
  }
});