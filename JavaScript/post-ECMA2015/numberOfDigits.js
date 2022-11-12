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

// Identifies if a number has one or two digits. If more digits, this program returns the number input back to you
