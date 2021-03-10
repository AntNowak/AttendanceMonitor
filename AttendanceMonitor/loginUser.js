//code based on tutorial: https://medium.com/swlh/how-to-create-your-first-login-page-with-html-css-and-javascript-602dd71144f1
//needs to be editied to work

const homepage = document.getElementById("homepage");
const homePage = document.getElementById("homepage-submit");
const loginErrorMsg = document.getElementById("homepage-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = homepage.username.value;
    const password = homepage.password.value;

    if (username === "user" && password === "web_dev"){
        alert("you have successfully been logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})





