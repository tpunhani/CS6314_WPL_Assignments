window.onload = function () {

    //there will be one span element for each input field
    // when the page is loaded, we create them and append them to corresponding input element 
    // they are initially empty and hidden

    var span1 = document.createElement("span");
    span1.style.display = "none"; //hide the span element
    var email = document.getElementById("email");
    email.parentNode.appendChild(span1);

    //Password span element

    var span2 = document.createElement("span");
    span2.style.display = "none"; //hide the span element
    var pass = document.getElementById("pwd");
    pass.parentNode.appendChild(span2);

    //confirm password span element

    var span3 = document.createElement("span");
    span3.style.display = "none"; //hide the span element
    var confirmPass = document.getElementById("confirm");
    confirmPass.parentNode.appendChild(span3);

    email.onfocus = function () {
        span1.innerHTML = "<p>The email field should be a valid email address (abc@def.xyz)</p>"
        email.classList.remove("error");
        span1.style.display = "";
    }

    email.onblur = function () {
        span1.style.display = "none";

    }


    pass.onfocus = function () {
        span2.innerHTML = "<p>The password field should contain at least six characters.</p>"
        pass.classList.remove("error");
        confirmPass.classList.remove("error");
        span2.style.display = "";
        span3.style.display = "none";

    }

    pass.onblur = function () {
        span2.style.display = "none";

    }


    confirmPass.onfocus = function () {
        span3.innerHTML = "<p>Re-enter your password</p>"
        confirmPass.classList.remove("error");
        pass.classList.remove("error");
        span3.style.display = "";
        span2.style.display = "none";
    }

    confirmPass.onblur = function () {
        span3.style.display = "none";
        if(pass.value != confirmPass.value){
            console.log("Confirm password field is not matched");
            pass.classList.add("error");
            confirmPass.classList.add("error");
            span3.innerHTML = "<p>Passwords do not match.</p>";
            span3.style.display = "";
        }
    }

    //calling custom method on document submission
    document.onsubmit = submitFunction;

    function submitFunction(event) {
        const expectedPattern = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/;
        console.log("email value: " + email.value);
        if (!expectedPattern.test(email.value)) {
            console.log("Email is incorrect");
            email.classList.add("error");
            span1.innerHTML = "<p>Please enter a valid email address: abc@def.xyz</p>"
            span1.style.display = "";
            event.preventDefault();
        }
        if (pass.value.length == 0) {
            console.log("Password is empty.");
            pass.classList.add("error");
            span2.innerHTML = "<p>Password field can't be left as blank.</p>";
            span2.style.display = "";
            event.preventDefault();
        }else if (pass.value.length < 6) {
            console.log("Password length is less than 6");
            pass.classList.add("error");
            span2.innerHTML = "<p>You should enter atleast 6 characters.</p>";
            span2.style.display = "";
            event.preventDefault();
        } else if (confirmPass.value != pass.value) {
            console.log("Confirm password field is not matched");
            pass.classList.add("error");
            confirmPass.classList.add("error");
            span3.innerHTML = "<p>Passwords do not match.</p>";
            span3.style.display = "";
            event.preventDefault();

        }
    }

}


