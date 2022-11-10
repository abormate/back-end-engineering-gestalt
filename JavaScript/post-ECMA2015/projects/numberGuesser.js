let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
const generateTarget = () => {
  return Math.floor(Math.random() * 9);
};
const compareGuesses = (humanGuess, computerGuess, secretTarget) => {
  diffHuman = Math.abs(secretTarget - humanGuess);
  diffComputer = Math.abs(secretTarget - computerGuess);
  if (diffHuman < diffComputer) {
    return true
  } else if (diffHuman > diffComputer) {
    return false
  } else {
    return true
  }
};

const updateScore = (stringWinner) => {
  if (stringWinner === 'human') {
    humanScore +=1;
  } else {
    computerScore +=1;
  }
};

const advanceRound = () => {
  currentRoundNumber +=1;
};



