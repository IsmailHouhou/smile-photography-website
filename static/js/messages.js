rightContainer = document.getElementsByClassName("right-container");
for (i = 0; i < rightContainer.length; i++) {
    rightContainer[i].style.display = "none";
}

function readMessage(event, clientName) {
    var i, messageDemo, rightContainer;

    rightContainer = document.getElementsByClassName("right-container");
    for (i = 0; i < rightContainer.length; i++) {
        rightContainer[i].style.display = "none";
    }

    messageDemo = document.getElementsByClassName("message-demo");
    for (i = 0; i <messageDemo.length; i++) {
        messageDemo[i].className = messageDemo[i].className.replace(" active", "")
    }
    
    document.getElementById(clientName).style.display = "flex";
    event.currentTarget.className += " active";
}