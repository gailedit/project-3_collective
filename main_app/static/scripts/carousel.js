// project carousel
const project_carousel = document.querySelector('#project-carousel');
const project_slider = document.querySelector('#project-slider');

const project_next = document.querySelector('#project-next-btn');
const project_prev = document.querySelector('#project-prev-btn');
let direction;

project_next.addEventListener('click', function() {
  direction = -1;
  project_carousel.style.justifyContent = 'flex-start';
  project_slider.style.transform = 'translate(-30%)';  
});

project_prev.addEventListener('click', function() {
  if (direction === -1) {
    direction = -1;
    project_slider.prependChild(project_slider.firstElementChild);
  }
  project_carousel.style.justifyContent = 'flex-end';    
  project_slider.style.transform = 'translate(30%)';  
  
});

project_slider.addEventListener('transitionend', function() {
  // get the last element and prepend it to the front
  
  if (direction === 1) {
    project_slider.prepend(project_slider.lastElementChild);
  } else {
    project_slider.appendChild(project_slider.firstElementChild);
  }

  project_slider.style.transition = 'none';
  project_slider.style.transform = 'translate(0)';
  setTimeout(() => {
    project_slider.style.transition = 'all 0.5s';
  })
}, false);

// profile carousel
const profile_carousel = document.querySelector('#profile-carousel');
const profile_slider = document.querySelector('#profile-slider');

const profile_next = document.querySelector('#profile-next-btn');
const profile_prev = document.querySelector('#profile-prev-btn');
let direction;

profile_next.addEventListener('click', function() {
  direction = -1;
  profile_carousel.style.justifyContent = 'flex-start';
  profile_slider.style.transform = 'translate(-30%)';  
});

profile_prev.addEventListener('click', function() {
  if (direction === -1) {
    direction = -1;
    profile_slider.prependChild(profile_slider.firstElementChild);
  }
  profile_carousel.style.justifyContent = 'flex-end';    
  profile_slider.style.transform = 'translate(30%)';  
  
});

profile_slider.addEventListener('transitionend', function() {
  // get the last element and prepend it to the front
  
  if (direction === 1) {
    profile_slider.prepend(profile_slider.lastElementChild);
  } else {
    profile_slider.appendChild(profile_slider.firstElementChild);
  }

  profile_slider.style.transition = 'none';
  profile_slider.style.transform = 'translate(0)';
  setTimeout(() => {
    profile_slider.style.transition = 'all 0.5s';
  })
}, false);