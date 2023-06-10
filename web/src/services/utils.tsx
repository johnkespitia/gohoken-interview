const removeDuplicates = (data:[string,string][]) => {
    const uniqueArr:[string,string][] = [];

    for (let i = 0; i < data.length; i++) {
        const currentItem = data[i];

        const alreadyExists = uniqueArr.some(
            (item) => item[0] === currentItem[0] && item[1] === currentItem[1]
        );

        if (!alreadyExists) {
            uniqueArr.push(currentItem);
        }
    }
    return uniqueArr;
};

export { removeDuplicates }