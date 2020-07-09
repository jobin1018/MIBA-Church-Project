
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

// Scroll to top btn
const scrollToTopBtn = document.querySelector('.scroll-to-top-btn');

window.addEventListener('scroll', () => {
    let height = this.scrollY;
    // console.log(height);
    if (height < 400) {
        scrollToTopBtn.style.opacity = "0";
        scrollToTopBtn.style.pointerEvents = "none";
    } else {
        scrollToTopBtn.style.opacity = "1";
        scrollToTopBtn.style.pointerEvents = "all";
    }
})

scrollToTopBtn.addEventListener('click', (e) => {
    window.scrollTo(0, 0);
    e.preventDefault();
})
// Scroll to top btn ends

// Stop Yt on modal close 

// Ends