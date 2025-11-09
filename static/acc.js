// let a = document.querySelector("#password");
// let b = document.querySelector(".mm");

// a.addEventListener('keyup', () => {
//     let c = a.value;
//     if (c !== "") {
//         if (c.length < 8) {
//             b.innerHTML = "Password must contain at least 8 characters";
//             a.style.color = 'red';  
//         } else {
//             b.textContent = "Strong password ✔";
//             a.style.color = 'green';  
//         }
//     } else {
//         b.textContent = "";
//         a.style.color = 'black'; // reset when empty
//     }
// });
let pwd = document.querySelector("#password");
let confirmpwd = document.querySelector("#confirmpwd");
let msg = document.querySelector(".mm");
let form = document.querySelector("form");


pwd.addEventListener("keyup", () => {
    let c = pwd.value;

    if (c.length === 0) {
        msg.textContent = ""; 
        pwd.style.color = "black";
    }
    else if (c.length < 8) {
        msg.textContent = "Password should contain at least 8 characters ❌";
        msg.style.color = "red";
        pwd.style.color = "red";
    }
    else {
        msg.textContent = "Strong password ✔";
        msg.style.color = "green";
        pwd.style.color = "green";
    }
});

form.addEventListener("submit", (e) => {
    if (pwd.value.length < 8) {
        e.preventDefault();
        msg.textContent = "Password must be at least 8 characters";
        msg.style.color = "red";
    }
    else if (pwd.value !== confirmpwd.value) {
        e.preventDefault();
        msg.textContent = "Passwords do not match ❌";
        msg.style.color = "red";
    }
    else {
        msg.textContent = "Passwords match ✔";
        msg.style.color = "green";
        // form will submit normally (go to car.html)
    }
});
