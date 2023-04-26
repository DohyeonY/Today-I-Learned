// for (let i = 0; i < 5; i++) {
//   for (let j = 0; j <= i; j++) {
//     console.log('*')
//   }
//   console.log();
// }


let star = ''
for (let i = 0; i <5; i++) {
  for (let j = 0; j <= i; j++) {
    star += '*'
  }
  star += '\n'
}
console.log(star)