function ValidateEmail(inputText) {
    var regex = /[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    if(inputText.value.match(regex)) {
        alert("You have entered a valid mail address!");
        document.form1.text1.focus();
        return true;

    } else {
        alert("You have entered an invalid email address!")
        document.form1.text1.focus();
        return false;
    }
}