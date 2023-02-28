// HERO VIDEO
function showReel() {
    video_container = document.getElementsByClassName('reel-container');
    video_container[0].style.display = 'block';
    video_container[0].style.visibility = 'visible';
    video_container[0].style.opacity = '1';

    body = document.getElementsByTagName('body');
    body[0].style.overflowY = 'hidden';
}

function closeReel() {
    video_container = document.getElementsByClassName('reel-container');
    video_container[0].style.visibility = 'hidden';
    video_container[0].style.opacity = '0';

    video = document.getElementById('video');
    video.pause();
    video.currentTime = 0;
    video.load();

    body = document.getElementsByTagName('body');
    body[0].style.overflowY = 'auto';
}

// SERVICES CAROUSEL
let serviceIndex = 1;
showService(serviceIndex);

function plusServices(n) {
    showService(serviceIndex += n);
}

function currentService(n) {
    showService(slideIndex = n);
}

function showService(n) {
    let i;
    let services = document.getElementsByClassName("service-carousel");
    if (n > services.length) {
        serviceIndex = 1;
    }
    if (n < 1) {
        serviceIndex = services.length;
    }
    for (i = 0; i < services.length; i++) {
        services[i].style.display = "none";
    }
    services[serviceIndex-1].style.display = "block";
}