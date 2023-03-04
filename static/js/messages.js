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

function updateRead(id) {
    $.ajax({
        url: "{% url 'update-message-read' %}?message_id=" + id,
        type: "POST",
        data: {
          csrfmiddlewaretoken: "{{ csrf_token }}",
        },
        success: function(response, id) {
          // If the request was successful, update the page content
        //   $("#my-model-field").text(response.new_value);
            read = response.read;
            document.getElementById('message-'+id).style.backgroundColor = '#e8f6fa';
        },
        error: function(xhr, status, error) {
          // If the request failed, log the error
          console.log(error);
        }
      });

}