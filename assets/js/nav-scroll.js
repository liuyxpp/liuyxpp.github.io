// Small enhancements around Bootstrap's navigation behavior.
(function () {
  'use strict';

  var nav = document.querySelector('.navbar-custom');
  var collapse = document.getElementById('primary-navigation');
  var toggle = nav && nav.querySelector('.navbar-toggle');

  if (!nav) return;

  function updateScrolledState() {
    nav.classList.toggle('scrolled', window.pageYOffset > 20);
  }

  updateScrolledState();
  window.addEventListener('scroll', updateScrolledState, { passive: true });

  if (!collapse || !toggle || !window.jQuery) return;

  var $collapse = window.jQuery(collapse);
  var label = toggle.querySelector('.sr-only');

  $collapse.on('shown.bs.collapse', function () {
    toggle.setAttribute('aria-expanded', 'true');
    if (label) label.textContent = 'Close navigation menu';
  });

  $collapse.on('hidden.bs.collapse', function () {
    toggle.setAttribute('aria-expanded', 'false');
    if (label) label.textContent = 'Open navigation menu';
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && collapse.classList.contains('in')) {
      $collapse.collapse('hide');
      toggle.focus();
    }
  });
}());
