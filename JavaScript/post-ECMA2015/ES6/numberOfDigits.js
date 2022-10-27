const numberDigits = x => {
  if (x >= 0 && x < 10) {
    return `One digit: ${x}` 
  } else if (x >= 10 && x < 100) {
    return `Two digits: ${x}`
  } else {
    return `The number is: ${x}`
  }
}

console.log(numberDigits(7));
