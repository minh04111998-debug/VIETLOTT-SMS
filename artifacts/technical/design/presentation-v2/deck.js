document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.slide');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const counterCurrent = document.getElementById('currentSlideNum');
  const counterTotal = document.getElementById('totalSlideNum');
  
  let currentSlide = 0;
  
  if(counterTotal) counterTotal.innerText = slides.length;

  function updateSlides() {
    slides.forEach((slide, index) => {
      slide.classList.remove('active', 'past');
      if (index === currentSlide) {
        slide.classList.add('active');
      } else if (index < currentSlide) {
        slide.classList.add('past');
      }
    });
    
    if(counterCurrent) counterCurrent.innerText = currentSlide + 1;
  }

  function nextSlide() {
    if (currentSlide < slides.length - 1) {
      currentSlide++;
      updateSlides();
    }
  }

  function prevSlide() {
    if (currentSlide > 0) {
      currentSlide--;
      updateSlides();
    }
  }

  if (prevBtn) prevBtn.addEventListener('click', prevSlide);
  if (nextBtn) nextBtn.addEventListener('click', nextSlide);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      prevSlide();
    }
  });

  // Initialize
  updateSlides();
});
