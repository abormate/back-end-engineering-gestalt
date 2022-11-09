const sortYears = array => array.sort((x,y) => y - x);

const years = [1970, 1999, 1951, 1982, 1963, 2011, 2018, 1922]

console.log(sortYears(years))

// prints out a list of numbers/years arranged in the descending order. By default sort() arranges items alphabetically in ascending order.  
