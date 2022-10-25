function finalGrade(score1, score2, score3) {
  average = (score1 + score2 + score3) / 3;
  if ((score1 < 0 || score1 > 100) || (score2 < 0 || score2 > 100) || (score3 < 0 || score3 > 100)) {
    return 'You have entered an invalid grade.'
  } else if (average < 60) {
    return 'F'
  } else if (average < 70) {
    return 'D'
  } else if (average < 80) {
    return 'C'
  } else if (average < 90) {
    return 'B'
  } else {
    return 'A'
  }
};
