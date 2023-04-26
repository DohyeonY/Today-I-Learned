function palindrome(str) {
  for (let i = 0; i < Math.floor(str.length / 2); i++) {
    let left = str[i]
    let right = str[str.length -1 -i]
    if (left != right) {
      return console.log('False')
    }
  }
  return console.log('True')
}

palindrome('tomato')
palindrome('beeb')