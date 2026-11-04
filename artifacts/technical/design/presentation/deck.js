/* ==========================================================================
   VIETLOTT SMS 2.0 PRESENTATION DECK ENGINE (INTERACTIVE JAVASCRIPT)
   Keyboard Navigation, Touch Controls, Progress Bar, Overview Modal, Fullscreen
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.slide');
  const totalSlides = slides.length;
  let currentSlideIndex = 0;

  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const currentSlideNumEl = document.getElementById('currentSlideNum');
  const totalSlideNumEl = document.getElementById('totalSlideNum');
  const progressBarFill = document.getElementById('progressBarFill');
  const fullscreenBtn = document.getElementById('fullscreenBtn');
  const overviewBtn = document.getElementById('overviewBtn');
  const overviewModal = document.getElementById('overviewModal');
  const closeOverviewBtn = document.getElementById('closeOverviewBtn');
  const overviewGrid = document.getElementById('overviewGrid');

  if (totalSlideNumEl) {
    totalSlideNumEl.textContent = totalSlides;
  }

  // Initialize Overview Modal Items
  slides.forEach((slide, idx) => {
    const titleEl = slide.querySelector('.slide-title') || slide.querySelector('.cover-main-title');
    const titleText = titleEl ? titleEl.textContent.trim() : `Slide ${idx + 1}`;

    const item = document.createElement('div');
    item.className = 'overview-item';
    item.innerHTML = `
      <div class="overview-item-num">SLIDE ${idx + 1}</div>
      <div class="overview-item-title">${titleText}</div>
    `;
    item.addEventListener('click', () => {
      goToSlide(idx);
      closeOverview();
    });
    overviewGrid.appendChild(item);
  });

  function updateDeckUI() {
    slides.forEach((slide, idx) => {
      slide.classList.remove('active', 'prev', 'next');
      if (idx === currentSlideIndex) {
        slide.classList.add('active');
      } else if (idx < currentSlideIndex) {
        slide.classList.add('prev');
      } else {
        slide.classList.add('next');
      }
    });

    if (currentSlideNumEl) {
      currentSlideNumEl.textContent = currentSlideIndex + 1;
    }

    if (progressBarFill) {
      const percentage = ((currentSlideIndex + 1) / totalSlides) * 100;
      progressBarFill.style.width = `${percentage}%`;
    }

    if (prevBtn) prevBtn.disabled = currentSlideIndex === 0;
    if (nextBtn) nextBtn.disabled = currentSlideIndex === totalSlides - 1;
  }

  function goToSlide(index) {
    if (index >= 0 && index < totalSlides) {
      currentSlideIndex = index;
      updateDeckUI();
    }
  }

  function nextSlide() {
    if (currentSlideIndex < totalSlides - 1) {
      currentSlideIndex++;
      updateDeckUI();
    }
  }

  function prevSlide() {
    if (currentSlideIndex > 0) {
      currentSlideIndex--;
      updateDeckUI();
    }
  }

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => {
        console.error(`Error attempting to enable fullscreen: ${err.message}`);
      });
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }

  function openOverview() {
    if (overviewModal) {
      overviewModal.classList.add('open');
    }
  }

  function closeOverview() {
    if (overviewModal) {
      overviewModal.classList.remove('open');
    }
  }

  function toggleOverview() {
    if (overviewModal) {
      if (overviewModal.classList.contains('open')) {
        closeOverview();
      } else {
        openOverview();
      }
    }
  }

  // Event Listeners
  if (nextBtn) nextBtn.addEventListener('click', nextSlide);
  if (prevBtn) prevBtn.addEventListener('click', prevSlide);
  if (fullscreenBtn) fullscreenBtn.addEventListener('click', toggleFullscreen);
  if (overviewBtn) overviewBtn.addEventListener('click', openOverview);
  if (closeOverviewBtn) closeOverviewBtn.addEventListener('click', closeOverview);

  // Keyboard Navigation
  document.addEventListener('keydown', (e) => {
    if (overviewModal && overviewModal.classList.contains('open')) {
      if (e.key === 'Escape' || e.key === 'o' || e.key === 'O') {
        closeOverview();
      }
      return;
    }

    switch (e.key) {
      case 'ArrowRight':
      case 'ArrowDown':
      case 'PageDown':
      case ' ':
        e.preventDefault();
        nextSlide();
        break;
      case 'ArrowLeft':
      case 'ArrowUp':
      case 'PageUp':
      case 'Backspace':
        e.preventDefault();
        prevSlide();
        break;
      case 'Home':
        e.preventDefault();
        goToSlide(0);
        break;
      case 'End':
        e.preventDefault();
        goToSlide(totalSlides - 1);
        break;
      case 'o':
      case 'O':
        e.preventDefault();
        toggleOverview();
        break;
      case 'f':
      case 'F':
        e.preventDefault();
        toggleFullscreen();
        break;
    }
  });

  // Touch Swipe Support for Mobile Devices
  let touchStartX = 0;
  let touchEndX = 0;

  document.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, false);

  document.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  }, false);

  function handleSwipe() {
    const swipeThreshold = 50;
    if (touchEndX < touchStartX - swipeThreshold) {
      nextSlide();
    }
    if (touchEndX > touchStartX + swipeThreshold) {
      prevSlide();
    }
  }

  // Initial UI Render
  updateDeckUI();
});
