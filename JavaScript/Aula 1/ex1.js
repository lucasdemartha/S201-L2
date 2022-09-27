function fillArray(arr) {
    for (let i = 0; i < 10; i++) {
        arr[i] = i + 1;
    }
    return arr;
}


let arr = [];
fillArray(arr);
console.log(arr);