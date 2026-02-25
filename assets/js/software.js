// Software page: smooth scroll for TOC + active state tracking

document.addEventListener('DOMContentLoaded', function () {
  const tocPills = document.querySelectorAll('.toc-pill');
  const categorySections = document.querySelectorAll('.category-section');

  // Smooth scroll on click
  tocPills.forEach(pill => {
    pill.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const target = document.getElementById(targetId);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        // Update active state
        tocPills.forEach(p => p.classList.remove('active'));
        this.classList.add('active');
      }
    });
  });

  // Active state tracking on scroll
  const observerOptions = {
    root: null,
    rootMargin: '-80px 0px -60% 0px',
    threshold: 0
  };

  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        tocPills.forEach(pill => {
          pill.classList.toggle('active', pill.getAttribute('href') === '#' + id);
        });
      }
    });
  }, observerOptions);

  categorySections.forEach(section => {
    observer.observe(section);
  });

  // Animate cards on scroll
  const cards = document.querySelectorAll('.software-card');
  const cardObserver = new IntersectionObserver(function (entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        cardObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  cards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    cardObserver.observe(card);
  });
});
