export const renderValidationLabel = (isValid, element, customError) => {
    try {
        const errorLabel = element.concat('_err')
        const el = document.querySelector(`#${errorLabel}`);

        if(!el) {
            return console.error('renderValidationLabel | element not found')
        }
        if(isValid && el) {
            return removeErrorStyle(el);
        }
        if(!isValid && el && customError ) {
            return applyErrorStyle(el, customError)
        }
    } catch (e) {
        console.error(`renderValidationLabel error : ${e}`)
    }
}


const applyErrorStyle = (element, customError) => {
    element.style.color = 'red';
    if(!customError) {
        element.innerHTML = "ERROR!";
    }
    element.innerHTML = customError.toString();
}

export const removeErrorStyle = (element) => {
    element.innerHTML = "";
}