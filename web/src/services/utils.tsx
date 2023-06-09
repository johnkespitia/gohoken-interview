const removeDuplicates = (data) => {
    const uniqueArr = [];

    for (let i = 0; i < data.length; i++) {
        const currentItem = data[i];

        const alreadyExists = uniqueArr.some(
            (item) => item[0] === currentItem[0] && item[1] === currentItem[1]
        );

        if (!alreadyExists) {
            uniqueArr.push(currentItem);
        }
    }

    console.log(uniqueArr);
    return uniqueArr;
};

export { removeDuplicates }