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