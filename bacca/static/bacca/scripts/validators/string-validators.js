export const minLengthValidator = (str, length) => {
    if(str && typeof str === 'string') {
        return str.trim().length >= length
    }
    return false;
}

export const validEmailValidator = (str) => {
    if(str){
        const emailRegex = /^[a-z0-9._]+@[a-z0-9-]+\.[a-z]{2,3}(\.[a-z]{2})?$/;
        const isValidEmail = emailRegex.test(str.toLowerCase());
        if(isValidEmail){
            return isValidEmail;
        }
        return false;
    }

}