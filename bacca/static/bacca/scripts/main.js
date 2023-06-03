import { VALIDATION_RULES } from "./constants/validation-rules.js";
import { renderValidationLabel } from "./services/render-validation.service.js";
import { inputExtractor } from "./utils/form.utils.js";
import { toggleVisibility } from "./utils/ui.utils.js";

// forms -> DOM references
const loginFormElement = document.querySelector("#login-form");
const contactFormElement = document.querySelector("#contact-form");

const areAllInputsValid = (validationArr) => {
    return validationArr.every(value => value === true);
}

const bindEventListenerToForm = (formElement, prefix, eventType, onSuccessFn) =>
{
    return formElement.addEventListener(eventType, event => eventHandler(event, prefix, onSuccessFn));
}

const eventHandler = (event, prefix, onSuccessFn) => {
    if (event){
        event.preventDefault();
        const { target: { elements } } = event;
        const inputs = inputExtractor(elements, prefix);

        if (inputs) {
            const allValid = validatorRunner(inputs);
            if(allValid && onSuccessFn) {
                onSuccessFn?.();
            }
        }
    }
}
const validatorRunner = (inputs) => {
    const loginInputValidations = [];
    for (let input in inputs) {
        const value = inputs[input];
        const { validatorFn, customError } = VALIDATION_RULES[input];
        if(validatorFn){
            const result = validatorFn?.(value);
            loginInputValidations.push(Boolean(result));
            customError ? renderValidationLabel(result, input, customError) : renderValidationLabel(result, input);
        }
    }
    const allValid = areAllInputsValid(loginInputValidations);
    if(!allValid){
        return console.log('[FORM VALIDATOR ERROR!] No se enviará al servidor');
    }
    return allValid;
}

// handler del formulario de contacto de la página principal
const contactFormHandler = () => {
    const onSuccessFn = () => {
        console.log('[FORM VALIDATOR OK!] Enviando al servidor...');
        setTimeout(() => {
            console.log('[FORM VALIDATOR: RESPUESTA SERVIDOR] Formulario recibido!');
        }, 1000)
    }
    const elementPrefix = "usr";
    bindEventListenerToForm(contactFormElement, elementPrefix, "submit", onSuccessFn);
}

// handler del formulario de login

const loginFormHandler = () => {
    const elementPrefix = "login";
    const eventType = "submit";
    const onSuccessFn = () => {
        loginFn();
        loginFormHideToggle();
        console.log('[FORM VALIDATOR OK!] Enviando al servidor...');
        setTimeout(() => {
            console.log('[FORM VALIDATOR: RESPUESTA SERVIDOR] Formulario recibido!');
        }, 1000)
    }
    bindEventListenerToForm(loginFormElement, elementPrefix, eventType, onSuccessFn);
}

const loginFormHideToggle = () => {
    const loginForm = document.querySelector('.form-container');
    const blurFilter = document.getElementById('blur-filter');
    const bodyWrapper = document.querySelector('body');
    const isOverflowHidden = bodyWrapper.style.overflow === 'hidden' ? true : false;

    toggleVisibility(loginForm);
    toggleVisibility(blurFilter);
    
    if(isOverflowHidden) {
        bodyWrapper.style.setProperty('overflow','auto')
    } else {
        bodyWrapper.style.setProperty('overflow','hidden');
    }
}

// conmutador del formulario login
const toggleLoginForm = () => {
    const cancelBtn = document.querySelector('.cancel-btn');
    const loginBtn = document.getElementById('login-form-btn');

    loginBtn.addEventListener('click', (event) => {
        event.preventDefault();
        loginFormHideToggle();
    })

    cancelBtn.addEventListener('click', (event) => {
        event.preventDefault();
        const inputsToClean = ['login_email','login_clave'];
        inputsToClean.forEach(element => renderValidationLabel(true, element));
        loginFormHideToggle();
    })
}

const loginFn = () => {
    const loginElement = document.querySelector('.nav-login');
    const logoutElements = document.querySelectorAll('.nav-logout');
    const emailValue = document.getElementById('login_email').value;
    const userEmail = document.getElementById('user-email');
    userEmail.innerText = emailValue;
    loginElement.style.display = 'none';
    logoutElements.forEach(element => element.style.display = 'block');
}

const logoutFn = () => {
    const logoutBtn = document.getElementById('logout-btn');
    const loginElement = document.querySelector('.nav-login');
    const logoutElements = document.querySelectorAll('.nav-logout');

    logoutBtn.addEventListener('click', (event) => {
        event.preventDefault();
        logoutElements.forEach(element => element.style.display = 'none');
        loginElement.style.display = 'block';
    })
}

// fix para svg externo con animación de path
const dynamicSvgFix = () => {
    const svgHolder = document.querySelector('object#dynamic-svg');
    svgHolder.onload = () => {
        const svgDocument = svgHolder.contentDocument;
        const style = svgDocument.createElementNS("http://www.w3.org/2000/svg", "style");
        style.textContent = '@import url("producto_animado.css");';
        const svgElem = svgDocument.querySelector('svg');
        svgElem.insertBefore(style, svgElem.firstChild);
    };
}

// ejecuciones:

dynamicSvgFix();
contactFormHandler();
toggleLoginForm();
loginFormHandler();
logoutFn();