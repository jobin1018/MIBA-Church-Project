
// MenuToggle script 
const mainNav = document.querySelector('.nav-container'),
    burgerMenu = document.querySelector('.burger-menu'),
    nonHomeHeader = document.querySelector('.non-home-header'),
    galleryDetailHeader = document.querySelector('.gallery-detail-header'),
    hubDetailHeader = document.querySelector('.gallery-detail-header');


burgerMenu.addEventListener('click', function () {
    mainNav.classList.toggle('open');
    nonHomeHeader.classList.toggle('active-header');
    hubDetailHeader.classList.toggle('active-header');
    galleryDetailHeader.classList.toggle('active-header');
});

//Scroll into view
document.querySelectorAll('.scroll-down-btn a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
