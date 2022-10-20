const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
	// 작성해 주세요
  for ( i = 0; i < 10; i++ ) {
    if ( p1[i] === p2[i] ) {
      console.log('0')
    }  
    else if ( p1[i] === 'rock' && p2[i] === 'scissors') {
      console.log('1')
    }
    else if ( p1[i] === 'rock' && p2[i] === 'papper') {
      console.log('2')
    }
    else if ( p1[i] === 'papper' && p2[i] === 'rock') {
      console.log('1')
    }
    else if ( p1[i] === 'papper' && p2[i] === 'scissors') {
      console.log('2')
    }
    else if ( p1[i] === 'scissors' && p2[i] === 'papper') {
      console.log('1')
    }
    else if ( p1[i] === 'scissors' && p2[i] === 'rock') {
      console.log('2')
    }
  }
}
playGame()
// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2