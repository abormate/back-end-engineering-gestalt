const isTheDinnerVegan = array => {
const isVegan = (food) => {
  if (food.source === 'plant') {
    return true;
  } 
  return false;
}

for(let i = 0; i<array.length; i++){
            if (!isVegan(array[i])){
                  return false 
            }
      }
      return true
}


const meal = [{name: 'arugula', source: 'plant'}, {name: 'tomatoes', source: 'plant'}, {name: 'lemon', source:'plant'}, {name: 'olive oil', source: 'plant'}];
 
console.log(isTheDinnerVegan(meal));
