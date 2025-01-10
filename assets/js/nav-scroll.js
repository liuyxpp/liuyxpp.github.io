// Nav bar scroll behavior
document.addEventListener('scroll', function() {
  const nav = document.querySelector('.nav_cleanblog');
  if (window.scrollY > 50) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }
});
