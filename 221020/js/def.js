const treeArgs = function (arg1, arg2, arg3) {
  return [arg1, arg2, arg3]
}

console.log(treeArgs())
console.log(treeArgs(1))
console.log(treeArgs(1, 2))


const noArgs = function () {
  return 0
}

console.log(noArgs(1, 2, 3))