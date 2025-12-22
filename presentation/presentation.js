// Presentation Slide Navigation

let currentSlide = 1;
const totalSlides = 5;

// Initialize AOS
AOS.init({
  duration: 800,
  easing: 'ease-in-out',
  once: false,
  mirror: true
});

// Update slide indicator
function updateSlideIndicator() {
  document.getElementById('currentSlide').textContent = currentSlide;
  document.getElementById('totalSlides').textContent = totalSlides;
  
  // Update navigation buttons
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  
  prevBtn.disabled = currentSlide === 1;
  nextBtn.disabled = currentSlide === totalSlides;
}

// Change slide
function changeSlide(direction) {
  const newSlide = currentSlide + direction;
  
  if (newSlide < 1 || newSlide > totalSlides) {
    return;
  }
  
  // Remove active class from current slide
  const currentSlideElement = document.querySelector(`.slide[data-slide="${currentSlide}"]`);
  currentSlideElement.classList.remove('active');
  
  // Add prev class for animation
  if (direction > 0) {
    currentSlideElement.classList.add('prev');
  }
  
  // Update current slide
  currentSlide = newSlide;
  
  // Add active class to new slide
  const newSlideElement = document.querySelector(`.slide[data-slide="${currentSlide}"]`);
  newSlideElement.classList.remove('prev');
  newSlideElement.classList.add('active');
  
  // Update indicator
  updateSlideIndicator();
  
  // Refresh AOS animations
  setTimeout(() => {
    AOS.refresh();
  }, 100);
}

// Go to specific slide
function goToSlide(slideNumber) {
  if (slideNumber < 1 || slideNumber > totalSlides) {
    return;
  }
  
  if (slideNumber === currentSlide) {
    return;
  }
  
  // Remove active class from current slide
  const currentSlideElement = document.querySelector(`.slide[data-slide="${currentSlide}"]`);
  currentSlideElement.classList.remove('active');
  
  // Add prev class for animation if going forward
  if (slideNumber > currentSlide) {
    currentSlideElement.classList.add('prev');
  }
  
  // Update current slide
  currentSlide = slideNumber;
  
  // Add active class to new slide
  const newSlideElement = document.querySelector(`.slide[data-slide="${currentSlide}"]`);
  newSlideElement.classList.remove('prev');
  newSlideElement.classList.add('active');
  
  // Update indicator
  updateSlideIndicator();
  
  // Scroll to top of slide
  newSlideElement.scrollTop = 0;
  
  // Refresh AOS animations
  setTimeout(() => {
    AOS.refresh();
  }, 100);
}

// Keyboard navigation
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') {
    changeSlide(-1);
  } else if (e.key === 'ArrowRight') {
    changeSlide(1);
  } else if (e.key === 'Home') {
    // Go to first slide
    while (currentSlide > 1) {
      changeSlide(-1);
    }
  } else if (e.key === 'End') {
    // Go to last slide
    while (currentSlide < totalSlides) {
      changeSlide(1);
    }
  }
});

// Touch/swipe support for mobile
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', (e) => {
  touchStartX = e.changedTouches[0].screenX;
});

document.addEventListener('touchend', (e) => {
  touchEndX = e.changedTouches[0].screenX;
  handleSwipe();
});

function handleSwipe() {
  const swipeThreshold = 50;
  const diff = touchStartX - touchEndX;
  
  if (Math.abs(diff) > swipeThreshold) {
    if (diff > 0) {
      // Swipe left - next slide
      changeSlide(1);
    } else {
      // Swipe right - previous slide
      changeSlide(-1);
    }
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  updateSlideIndicator();
  
  // Set first slide as active
  const firstSlide = document.querySelector('.slide[data-slide="1"]');
  if (firstSlide) {
    firstSlide.classList.add('active');
  }
  
  // Refresh AOS after a short delay to ensure all elements are rendered
  setTimeout(() => {
    AOS.refresh();
  }, 300);
});

// Handle window resize
window.addEventListener('resize', () => {
  AOS.refresh();
});

