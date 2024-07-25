document.getElementById('loginform').addEventListener('submit', function (event) {

    var enteredEmail = document.getElementById('username').value;
    var enteredPassword = document.getElementById('password').value;

    var storedEmail = localStorage.getItem('userEmail');
    var storedPassword = localStorage.getItem('userPassword');
    var name = document.getElementById("email").value

    if (enteredEmail === storedEmail && enteredPassword === storedPassword) {
        alert(`Welcome ${name}!`);
        
    } else {
        event.preventDefault();
        alert('Invalid email or password. Please try again.');
    }
});