document.addEventListener('DOMContentLoaded', () => {
    const navbarToggle = document.querySelector('.navbar-toggle');
    const navbar = document.querySelector('.navbar');

    navbarToggle.addEventListener('click', () => {
        navbar.classList.toggle('active');
    });
});
