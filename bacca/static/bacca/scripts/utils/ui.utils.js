export const toggleVisibility = (HTMLElement) => {
    HTMLElement.style.visibility === 'hidden' || HTMLElement.style.cssText === ''
        ? HTMLElement.style.visibility = 'visible'
        : HTMLElement.style.visibility = 'hidden';
}