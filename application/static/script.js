/**
 * Scripts for index, login, and register.
 */

function login() {
    fetch("/auth/login")
        .then(response => response.text())
        .then(html => {
            document.body.innerHTML = html;
        })
        .catch(error => {
            console.error("Error: ", error)
        });
}

function register() {
    fetch("/auth/register")
        .then(response => response.text())
        .then(html => {
            document.body.innerHTML = html;
        })
        .catch(error => {
            console.log("Error: ", error)
        });
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

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
    });

    if (response.redirected) {
        window.location.href = response.url;
    } else {
        window.location.reload();
    }
}

async function loginUser(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
    });

    if (response.redirected) {
        window.location.href = response.url;
    } else {
        window.location.reload();
    }
}
