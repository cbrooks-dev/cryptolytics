function login() {
    fetch("/login")
        .then(response => response.json())
        .then(data => {
            alert(data.message)
        })
        .catch(error => {
            console.error("Error: ", error)
        });
}


function register() {
    fetch("/register")
        .then(response => response.json())
        .then(data => {
            alert(data.message)
        })
        .catch(error => {
            console.log("Error: ", error)
        });
}
