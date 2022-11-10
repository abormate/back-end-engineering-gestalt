const speciesArray = [ {speciesName:'shark', numTeeth:50}, {speciesName:'dog', numTeeth:42}, {speciesName:'alligator', numTeeth:80}, {speciesName:'human', numTeeth:32}];

// Write your code here:
const sortSpeciesByTeeth = array =>
  array.sort((speciesObj1, speciesObj2) => speciesObj1.numTeeth > speciesObj2.numTeeth);






// test function

console.log(sortSpeciesByTeeth(speciesArray))
