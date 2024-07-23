// Send Mail starts

function sendMail(){
    (function(){
        emailjs.init("_1ooFWUwSokQXtCk_");
    })();

    var appointmentDate = document.getElementById("appointmentDate").value;
    var appointmentTime = document.getElementById("appointmentTime").value;
    // Combine date and time strings and create a Date object
    var appointmentDateTime = new Date(appointmentDate + "T" + appointmentTime);
    var reminderTime = new Date(appointmentDateTime.getTime() - (1 * 60 * 60 * 1000));

    var params = {
        sendername : "Janani Jivan",
        to : document.querySelector("#to").value,
        subject : "Reminder for your Next Appointment with Dr. Khatpatiya!",
        replyto : "noreply@gmail.com",
        message : "Reminder: Your appointment on " + appointmentDate + " at " + appointmentTime + " is coming up in one hour!",
    }

    var serviceID = "service_99t6xdd";
    var templateID = "template_gionilb";

    setTimeout(function() {
        emailjs.send(serviceID, templateID, params)
    }, reminderTime - Date.now());
    alert("Appointment Scheduled Successfully!");
}

// Send Mail ends