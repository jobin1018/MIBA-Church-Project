
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