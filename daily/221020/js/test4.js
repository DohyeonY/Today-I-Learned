const users = [
    { name: 'John', age: 31, isMarried: true, balance: 100, },
    { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
    { name: 'Ashley', age: 25, isMarried: true, balance: 300, },
    { name: 'Robert', age: 27, isMarried: false, balance: 400, },
    { name: 'Tom', age: 35, isMarried: true, balance: 500, },
  ]




// let user = function (users) {
//     console.log(user)
//   }
// users.forEach((user) => {
//     return `${console.log(user.name)}`
//   })

// const userFilter = function (user) {
//     return user.isMarried === true
  
//   }
// const married = users.filter(userFilter)
// console.log(married)
// const tom = users.find(function (tom) {
//     return tom.name === 'Tom'
//   })
// console.log(tom)
// let values = []
// const filter = users.map(data => ({
//     ...data, isAlive:'True'
// }))
// values = [...filter]
// console.log(values)

let sum = users.reduce((totalBalance, balance) => {
    return totalBalance += balance.balance
  }, 0)
  
console.log(sum)
  
