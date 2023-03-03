// NEEDS FIXING
function showProductsMenu() {
    menu = document.getElementById("products-menu");
    icon = document.getElementById("fa-icon-product");
    if (menu.classList.contains('show')) {
        menu.classList.remove("show");
        icon.classList.remove("fa-caret-up");
        icon.classList.add("fa-caret-down");
    } else if (!menu.classList.contains('show')) {
        menu.classList.add("show");
        icon.classList.remove("fa-caret-down");
        icon.classList.add("fa-caret-up");
    }
}

function showVideosMenu() {
    menu = document.getElementById("videos-menu");
    icon = document.getElementById("fa-icon-video");
    if (menu.classList.contains('show')) {
        menu.classList.remove("show");
        icon.classList.remove("fa-caret-up");
        icon.classList.add("fa-caret-down");
    } else if (!menu.classList.contains('show')) {
        menu.classList.add("show");
        icon.classList.remove("fa-caret-down");
        icon.classList.add("fa-caret-up");
    }
}

// COLORED ICON FOR SELECTED PAGE
navigation = document.getElementsByClassName('nav-row');
[].forEach.call(navigation, function(nav) {
    nav.style.filter = 'grayscale(100%)';
});
navigationDropdown = document.getElementsByClassName('nav-row-dropdown');
[].forEach.call(navigationDropdown, function(nav) {
    nav.style.filter = 'grayscale(100%)';
});
if (page == 'dashboard') {
    reservation = document.getElementById('dashboard');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#dashboard a');
    reservationText.style.color = '#fff';
} else if (page == 'add-product') {
    showProductsMenu();
    reservation = document.getElementById('products');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#products a');
    reservationText.style.color = '#fff';
    reservationText2 = document.querySelector('#products-menu a:nth-child(1)');
    reservationText2.style.color = '#fff';
} else if (page == 'products-list') {
    showProductsMenu();
    reservation = document.getElementById('products');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#products a');
    reservationText.style.color = '#fff';
    reservationText3 = document.querySelector('#products-menu a:nth-child(2)');
    reservationText3.style.color = '#fff';
} else if (page == 'add-video') {
    showVideosMenu();
    reservation = document.getElementById('videos');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#videos a');
    reservationText.style.color = '#fff';
    reservationText3 = document.querySelector('#videos-menu a:nth-child(1)');
    reservationText3.style.color = '#fff';
} else if (page == 'videos-list') {
    showVideosMenu();
    reservation = document.getElementById('videos');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#videos a');
    reservationText.style.color = '#fff';
    reservationText3 = document.querySelector('#videos-menu a:nth-child(2)');
    reservationText3.style.color = '#fff';
} else if (page == 'reservations-list') {
    reservation = document.getElementById('reservations');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#reservations a');
    reservationText.style.color = '#fff';
} else if (page == 'messages') {
    reservation = document.getElementById('messages');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#messages a');
    reservationText.style.color = '#fff';
}