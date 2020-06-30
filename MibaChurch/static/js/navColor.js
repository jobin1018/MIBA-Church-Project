const navBar = document.querySelector('.navbar'),
            navBarCollapse = document.querySelector('.navbar-collapse'),
            navTogglerBtn = document.querySelector('.navbar-toggler');

        navTogglerBtn.addEventListener('click', () => {
            navBar.classList.toggle('navbar-collapse-bg')
        });
        navTogglerBtn.addEventListener('click', () => {
            navBarCollapse.classList.toggle('navbar-collapse-bg')
        });
