function showMenu() {
    menu = document.getElementsByClassName('open-menu');
    menu[0].style.display = 'block';
    menu[0].style.visibility = 'visible';
    menu[0].style.opacity = '1';

    body = document.getElementsByTagName('body');
    body[0].style.overflowY = 'hidden';
}

function hideMenu() {
    menu = document.getElementsByClassName('open-menu');
    menu[0].style.visibility = 'hidden';
    menu[0].style.opacity = '0';

    body = document.getElementsByTagName('body');
    body[0].style.overflowY = 'scroll';
}