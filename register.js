document.getElementById("check").addEventListener("change", function togglePassword() {
    var passwordField = document.getElementById('password');
    var confirmField = document.getElementById('confirm');
    var checkbox = document.getElementById('check');

    if (checkbox.checked) {
        passwordField.type = 'text';
        confirmField.type = 'text';
    } else {
        passwordField.type = 'password';
        confirmField.type = 'password';
    }
} ) 


document.getElementById('registreform').addEventListener('submit', function (event) {

    var email = document.getElementById('emailid').value;
    var password = document.getElementById('password').value;
    var confirmpassword = document.getElementById('confirm').value;
    if(confirmpassword === password){

    localStorage.setItem('userEmail', email);
    localStorage.setItem('userPassword', password);

    alert('Registration successful! Please proceed to login.');
    } else{
        alert('Incorrect password')
    }

});

