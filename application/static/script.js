/**
 * Scripts for index, login, and register.
 */

function login() {
    window.location.href = "/auth/login"
}

function register() {
    window.location.href = "/auth/register"
}

function search() {
    fetch("/search")
        .then(response => response.json())
        .then(data => {
            alert(data.message)
        })
        .catch(error => {
            console.log("Error: ", error)
        });
}

async function registerUser(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`
    });

    if (response.redirected) {
        window.location.href = response.url;
    } else {
        window.location.reload();
    }
}

async function loginUser(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`
    });

    if (response.redirected) {
        window.location.href = response.url;
    } else {
        window.location.reload();
    }
}
