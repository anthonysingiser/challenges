/*
Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? not yet.*/

const numberK = Math.floor(Math.random () * 35)
const challengeArray = [10, 15, 3, 7, 17]

console.log(numberK)

//function takes in any array, 
//compares every two numbers to see if they add to k

function doTwoEqualK(num1, num2){
  if(num1 + num2 === numberK){
    console.log(num1, num2)
    return true
  }
  else{
    return false
  }
}

function existsInArray(array, num1){
  for(let w=0; w<array.length; w++){
    return doTwoEqualK(num1, array[w])
  }
}

function iterator(array){
  for (let i = 0; i < array.length; i++){
    if(existsInArray(array, array[i])){
      return true
    }
  }
return false
}

console.log(iterator(challengeArray))