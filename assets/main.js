(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
    // On mobile, first tap on a parent item opens its submenu
    nav.querySelectorAll('.has-sub > a').forEach(function (a) {
      a.addEventListener('click', function (e) {
        if (window.innerWidth > 1020) return;
        var li = a.parentElement;
        if (!li.classList.contains('open')) { e.preventDefault(); li.classList.add('open'); }
      });
    });
  }

  // Category cards: play a muted preview of the category video on hover (desktop only)
  if (window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('.cat-card[data-preview]').forEach(function (card) {
      var v;
      card.addEventListener('mouseenter', function () {
        if (!v) {
          v = document.createElement('video');
          v.muted = true; v.loop = true; v.playsInline = true; v.preload = 'auto';
          v.src = card.dataset.preview;
          v.setAttribute('aria-hidden', 'true');
          card.querySelector('.cat-media').appendChild(v);
        }
        v.currentTime = 0;
        v.play().then(function () { card.classList.add('playing'); }).catch(function () {});
      });
      card.addEventListener('mouseleave', function () {
        card.classList.remove('playing');
        if (v) v.pause();
      });
    });
  }

  // Only one video plays at a time
  document.addEventListener('play', function (e) {
    if (e.target.tagName !== 'VIDEO' || e.target.muted) return;
    document.querySelectorAll('video').forEach(function (o) { if (o !== e.target && !o.muted) o.pause(); });
  }, true);

  // Contact form: compose a WhatsApp message (no backend needed)
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var msg = 'Hi Coach Don, my name is ' + d.get('name') + '.\n' +
        'Service: ' + d.get('service') + '\nArea: ' + d.get('area') +
        (d.get('goal') ? '\nGoal: ' + d.get('goal') : '');
      window.open('https://wa.me/' + form.dataset.wa + '?text=' + encodeURIComponent(msg), '_blank', 'noopener');
    });
  }
})();
