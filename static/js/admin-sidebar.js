// FORM MESSAGES
$("#success-message").fadeOut(3000);
$("#warning-message").fadeOut(3000);

// DROP DOWN IN SIDEBAR
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
navigation = document.querySelectorAll('.nav-row img');
[].forEach.call(navigation, function(nav) {
    nav.style.filter = 'grayscale(100%)';
});
navigationDropdown = document.querySelectorAll('.nav-row-dropdown img');
[].forEach.call(navigationDropdown, function(nav) {
    nav.style.filter = 'grayscale(100%)';
});
if (page == 'dashboard') {
    reservation = document.querySelector('#dashboard img');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#dashboard a');
    reservationText.style.color = '#fff';
} else if (page == 'add-product') {
    showProductsMenu();
    reservation = document.querySelector('#products img');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#products a');
    reservationText.style.color = '#fff';
    reservationText2 = document.querySelector('#products-menu a:nth-child(1)');
    reservationText2.style.color = '#fff';
} else if (page == 'products-list') {
    showProductsMenu();
    reservation = document.querySelector('#products img');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#products a');
    reservationText.style.color = '#fff';
    reservationText3 = document.querySelector('#products-menu a:nth-child(2)');
    reservationText3.style.color = '#fff';
} else if (page == 'add-video') {
    showVideosMenu();
    reservation = document.querySelector('#videos img');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#videos a');
    reservationText.style.color = '#fff';
    reservationText3 = document.querySelector('#videos-menu a:nth-child(1)');
    reservationText3.style.color = '#fff';
} else if (page == 'videos-list') {
    showVideosMenu();
    reservation = document.querySelector('#videos img');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#videos a');
    reservationText.style.color = '#fff';
    reservationText3 = document.querySelector('#videos-menu a:nth-child(2)');
    reservationText3.style.color = '#fff';
} else if (page == 'reservations-list') {
    reservation = document.querySelector('#reservations img');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#reservations a');
    reservationText.style.color = '#fff';
} else if (page == 'messages') {
    reservation = document.querySelector('#messages img');
    reservation.style.filter = 'grayscale(0%)';
    reservationText = document.querySelector('#messages a');
    reservationText.style.color = '#fff';
}