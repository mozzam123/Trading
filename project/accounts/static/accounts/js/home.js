function openModal() {
    document.getElementById("strategyModal").style.display = "block";
}

function closeModal() {
    document.getElementById("strategyModal").style.display = "none";
}

function submitStrategy() {
    // Add your logic to handle form submission here
    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;

    // Add your logic to handle the data (e.g., send it to the server)
    console.log(username)
    console.log(email)
    // Close the modal after submission
    closeModal();
}