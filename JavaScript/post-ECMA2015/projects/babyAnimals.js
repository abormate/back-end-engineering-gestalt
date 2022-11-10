const animals = ['panda', 'turtle', 'giraffe', 'hippo', 'sloth', 'human'];

result = [];
const convertToBaby = array => {
  for (let i=0; i<array.length; i++) {
    result.push('baby ' + array[i]);
  }
  return result;
}
// When you're ready to test your code, uncomment the below and run:


console.log(convertToBaby(animals)) 
