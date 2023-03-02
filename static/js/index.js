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


function showThumbnail(id) {
    thumbnail_image = document.getElementById('thumbnail-'+id);
    thumbnail_name = document.getElementById('title-'+id);
    works = document.getElementsByClassName('works');

    thumbnail_name.addEventListener("mouseover", () => {
        thumbnail_image.style.display = "block";
        works[0].style.position = "relative";
      });
      
      thumbnail_name.addEventListener("mouseleave", () => {
        thumbnail_image.style.display = "";
    });

    window.addEventListener("mousemove", (e) => {
        let x = e.offsetX,
          y = e.offsetY;
      
        if (e.target == thumbnail_name) {
            thumbnail_image.style.left = `${x}px`;
            thumbnail_image.style.top = `${y}px`;
        } 
    });
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