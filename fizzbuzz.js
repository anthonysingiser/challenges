/*Write a function which prints every number from 0 up to the given input. 
If divisible by 3, print "Fizz" instead of the number. If divisible by 5, print "Buzz". 
If input is divisible by 3 AND 5, print "FizzBuzz".*/

/*
simplest problems: if divisible by 3 print 'Fizz', if divisible by 5 print 'Buzz'

return 'Fizz', 'Buzz' or 'FizzBuzz'

iterate from 0 to the given number

test each number

print for each number that passes

*/

//funny function to do it with isInteger instead of the modulo

function logFizzBuzzOrNumber(number){
  if(Number.isInteger(number/3) && Number.isInteger(number/5)){
    return console.log('FizzBuzz')
  }
  if(Number.isInteger(number/3)){
    return console.log('Fizz')
  }
  if(Number.isInteger(number/5)){
    return console.log('Buzz')
  }
  else{
    return console.log(number)
  }
}

function countFromZeroToGivenNumber(number){
    for(i=0; i<=number; i++){
        logFizzBuzzOrNumberWithModulo(i)
    }
}

function logFizzBuzzOrNumberWithModulo(number){
    if(number % 3 === 0 && number % 5 === 0){
        return console.log('FizzBuzz')
    }
    if(number % 3 === 0){
        return console.log('Fizz')
    }
    if(number % 5 === 0){
        return console.log('Buzz')
    }
    else{
        return console.log(number)
    }
}

countFromZeroToGivenNumber(100)
