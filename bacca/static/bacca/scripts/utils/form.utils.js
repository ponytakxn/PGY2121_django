
// utilitario de extracción de campos

export const inputExtractor = (inputCollection, prefix = "") => {
    if(inputCollection) {
        const inputArr = [...inputCollection];
        const filteredArr = inputArr.filter(input => input.name.startsWith(prefix));
        return filteredArr.reduce((acc, current) => {
            const { name, value, checked } = current;
            acc[name] = value || checked;
            return acc;
        },{})
    }
}

