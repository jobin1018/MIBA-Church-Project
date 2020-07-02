const navBar = document.querySelector('.navbar'),
    navBarCollapse = document.querySelector('.navbar-collapse'),
    navTogglerBtn = document.querySelector('.navbar-toggler'),
    nonHomeHeader = document.querySelector('.non-home-header'),
    galleryDetailHeader = document.querySelector('.gallery-detail-header');

navTogglerBtn.addEventListener('click', () => {
    navBar.classList.toggle('navbar-collapse-bg');
    navBarCollapse.classList.toggle('navbar-collapse-bg');
    nonHomeHeader.classList.toggle('active-header');
    hubDetailHeader.classList.toggle('active-header');
    galleryDetailHeader.classList.toggle('active-header');

});
