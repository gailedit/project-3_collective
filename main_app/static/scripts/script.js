/* === Responsive Navbar === */

const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

toggleButton.addEventListener('click', () => {
  navbarLinks.classList.toggle('active')
})

/* === Clicking Log In button pops up login modal === */

const loginButton = document.getElementById("login-btn");
loginButton.addEventListener("click", showLoginModal);

function showLoginModal() {
  console.log('click?');
  const login = document.getElementById("loginModal");
  if (login.style.display === "none") {
    login.style.display = "block";
  } else {
    login.style.display = "none";
  }
}

/* === Clicking Sign Up button pops up signup modal === */
const signUpButton = document.getElementById("signup-btn");

signUpButton.addEventListener("click", showSignUpModal);

function showSignUpModal() {
  console.log('clicked signup');
  const signup = document.getElementById("signUpModal");
  if (signup.style.display === "none") {
    signup.style.display = "block";
  } else {
    login.style.display = "none";
  }
}