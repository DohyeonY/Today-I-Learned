const name = '홍길동'

switch(name) {
  case '홍길동' :{
    console.log('관리자')
    break
  }
  case 'manager' :{
    console.log('매니저')
    break
  }
  default : {
    console.log(`${name}님`)

  }
}