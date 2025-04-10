
func buscaBinaria(arr: [Int], number: Int) -> Int {
    let baixo: Int = 0
    let meio: Int = (arr.count / 2) - 1
    let maior: Int = arr.count - 1

    while baixo <= maior {
        if number == arr[meio] {
            return meio
            break
        }
    }

    return 0
}

let arr = [2, 5, 6, 8, 10, 45, 80]

print(buscaBinaria(arr: arr, number: 8))
