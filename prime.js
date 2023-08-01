// -----------------------------------------------------------------
// BRUTE FORCE
// -----------------------------------------------------------------

function isPrime(num) {
    if (num <= 1) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
  
    for (let i = 3; i <= Math.sqrt(num); i += 2) {
      if (num % i === 0) return false;
    }
  
    return true;
  }
  
  function findNextPrimeAfterX(x) {
    let nextNum = x + 1;
    while (true) {
      if (isPrime(nextNum)) {
        return nextNum;
      }
      nextNum++;
    }
  }
  
  function primeNumberDifference(x) {
    if (isPrime(x)) {
      const nextPrime = findNextPrimeAfterX(x);
      return nextPrime - x;
    } else {
      return -1; // If x is not a prime number, return -1
    }
  }
  
  // Usage
  const y = 17;
  if (isPrime(y)) {
    console.log(y + " is a prime number.");
    const difference = primeNumberDifference(y);
    console.log("Difference between next prime and " + y + " is: " + difference);
  } else {
    console.log(y + " is not a prime number.");
  }


// -----------------------------------------------------------------
// OPTIMIZED APPROACH using the Sieve of Eratosthenes.
// -----------------------------------------------------------------

  function isPrime(num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
  
    if (num % 2 === 0 || num % 3 === 0) return false;
  
    let i = 5;
    while (i * i <= num) {
      if (num % i === 0 || num % (i + 2) === 0) return false;
      i += 6;
    }
  
    return true;
  }
  
  function findNextPrimeAfterX(x) {
    let nextNum = x + 1;
    while (true) {
      if (isPrime(nextNum)) {
        return nextNum;
      }
      nextNum++;
    }
  }
  
  function primeNumberDifference(x) {
    if (x < 2) return -1;
  
    if (isPrime(x)) {
      const nextPrime = findNextPrimeAfterX(x);
      return nextPrime - x;
    } else {
      return -1;
    }
  }
  
  // Usage
  const x = 17;
  const difference = primeNumberDifference(x);
  console.log("Difference between next prime and " + x + " is: " + difference);
  
  