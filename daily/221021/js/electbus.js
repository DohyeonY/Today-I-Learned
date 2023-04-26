//     K, N, M = list(map(int, input().split()))
//     station = list(map(int, input().split()))
//     now = 0
//     cnt = 0
 
//     while now + K < N :
 
//         for i in range(K, 0, -1):
//             # print(i)
//             if now + i in station :
//                 cnt += 1
//                 now = now + i
//                 # print(now)
//                 break
 
//         else :
//             cnt = 0
//             break
// const inputs = [
//   [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
//   [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
//   [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
// ]


// for (let i = 0; i < 3; i++) {
//   let now = 0
//   let cnt = 0
//   while (now + inputs[i][0] < inputs[i][1]) {
//     for (let j = inputs[i][0]; j > 0; j--) {
//       // console.log(now)
//       if (now + j in inputs[i][3]) {
//         console.log("rr")
//         cnt ++
//         now += j
//       }
//     }
//   }
  // console.log(cnt)
// }

const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  // solution 함수 완성
  let now = 0
  let cnt = 0
  while (now + K < N) {
    let flag = false
    for (let i = K; i > 0; i--) {
      if (chargers.includes(now + i) ) {
        cnt ++
        now += i
        flag = true
        break
      }
      
    }
    if (flag === false) {
      return console.log(0)
    }
  }
  return console.log(cnt)
}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}