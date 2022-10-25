function greetWorld() {
  return 'Hello, World!';
};

function canIVote(age) {
  if (age >= 18) {
    return true;
  } else {
    return false;
  }
};

function agreeOrDisagree(string1, string2) {
  if (string1 === string2) {
    return 'You agree!';
  } else {
    return 'You disagree!';
  }
};

// Write your function here:
function lifePhase(age) {
  if (age < 0 || age > 140 ) {
    return 'This is not a valid age'
  }
  else if (age < 4) {
    return 'baby'
  } else if (age < 13 ) {
    return 'child'
  } else if (age < 20) {
    return 'teen'
  } else if (age < 65) {
    return 'adult'
  } else {
    return 'senior citizen'
  }
};
