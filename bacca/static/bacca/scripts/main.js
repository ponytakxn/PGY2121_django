import { VALIDATION_RULES } from "./constants/validation-rules.js";
import { renderValidationLabel } from "./services/render-validation.service.js";
import { inputExtractor } from "./utils/form.utils.js";

// forms -> DOM references
const loginFormElement = document.querySelector("#login-form");
const contactFormElement = document.querySelector("#contact-form");

const areAllInputsValid = (validationArr) => {
    return validationArr.every(value => value === true);
}

const bindEventListenerToForm = (formElement, prefix, eventType, onSuccessFn) => {
    return formElement.addEventListener(eventType, event => eventHandler(event, prefix, onSuccessFn));
}

const eventHandler = (event, prefix, onSuccessFn) => {
    if (event) {
        event.preventDefault();
        const { target: { elements } } = event;
        const inputs = inputExtractor(elements, prefix);

        if (inputs) {
            const allValid = validatorRunner(inputs);
            if (allValid && onSuccessFn) {
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
        if (validatorFn) {
            const result = validatorFn?.(value);
            loginInputValidations.push(Boolean(result));
            customError ? renderValidationLabel(result, input, customError) : renderValidationLabel(result, input);
        }
    }
    const allValid = areAllInputsValid(loginInputValidations);
    if (!allValid) {
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