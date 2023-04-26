const nums = [1, 2, 3, 4]


const doubleFunc = function (num) {
  return num * num * num
}
const doubleNumbers = nums.map(doubleFunc)
console.log(doubleNumbers)