// const conda = new Snake({ name: 'conda' })
// const boa = new Snake({ name: 'boa' })

// console.log(conda.health)  // 100
// boa.bite(conda)
// console.log(conda.health)  // 90


class Monster {
  constructor(name) {
    this.name = name
    this.health = 100
  }
}

class Snake extends Monster {
  bite(another){
    another.health -= 10
  }
}

const conda = new Snake({ name: 'conda' })
const boa = new Snake({ name: 'boa' })

console.log(conda.health)  // 100
boa.bite(conda)
console.log(conda.health)  // 90
