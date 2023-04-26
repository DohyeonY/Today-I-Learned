let add = (x, y) => {
  return x + y
}
console.log(add(1,2))

const tom = {
  name: 'Tom',
  introduce () {
    console.log('Hi, my name is' + this.name)
  }
}
console.log(tom)


// const request = { url: url, data: data }
let request = {}
request['url'] = 'https://test.com'
request['data'] =  'message: Hello World! '
console.log(request)