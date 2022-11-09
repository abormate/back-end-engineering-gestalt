const shoutGreetings = array => {
  array.map(word => word.toUpperCase() + "!");
}

const greetings = ['hello', 'hi', 'heya', 'oi', 'hey', 'yo'];

console.log(shoutGreetings(greetings))
