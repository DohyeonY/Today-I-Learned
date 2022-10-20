let add = (x, y) => {
  return x + y
}
console.log(add(1,2))

const tom = {
  name: 'Tom',
  introduce: function () {
    console.log('Hi, my name is' + this.name)
  }
}
