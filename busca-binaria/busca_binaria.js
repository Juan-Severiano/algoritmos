
function buscaBinaria(arr, item) {
  let low = 0
  let high = arr.length - 1

  while (low <= high) {
    let middle = (low + high) / 2
    let value = arr[middle]

    if (value === item) {
      return middle
    }
    if (value > item) {
      middle ++
    }
    else {
      low = middle + 1
    }
  }
  return null
}

const arr = [
  1,3,5,7,9
]

console.log(buscaBinaria(arr, 3))
