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

// WORKS
// works popup
function showWork(id) {
    work = document.getElementById('work-'+id);
    work.style.display = 'block';
    work.style.visibility = 'visible';
    work.style.opacity = '1';

    body = document.getElementsByTagName('body');
    body[0].style.overflowY = 'hidden';
}

function closeWork(id) {
    work = document.getElementById('work-'+id);
    work.style.visibility = 'hidden';
    work.style.opacity = '0';

    video = document.getElementById('video-'+id);
    video.pause();
    video.currentTime = 0;
    video.load();

    body = document.getElementsByTagName('body');
    body[0].style.overflowY = 'auto';
}

// works onhover
function showImage(event, id) {
    var image = document.getElementById('thumbnail-image-'+id);
    image.style.left = event.clientX + "px";
    image.style.top = event.clientY + "px";
    image.style.display = "block";
}

function activateImage(id) {
    div = document.getElementsByClassName('thumbnail');
    div.forEach(element => {
        element.style.display = "none";
    });
    thumbnail = document.getElementById('thumbnail-image-'+id);
    thumbnail.style.display = 'block';
    thumbnail.parentElement.style.display = 'block';
}

function hideImage(id) {
    var image = document.getElementById('thumbnail-image-'+id);
    image.style.display = "none";
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