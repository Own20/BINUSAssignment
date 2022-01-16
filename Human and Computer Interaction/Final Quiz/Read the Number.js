// Write a function (and also the solution flowchart) that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that integer written in English.

// Examples
    // numToEng(0) ➞ "zero" 
    // numToEng(18) ➞ "eighteen" 
    // numToEng(126) ➞ "one hundred twenty six" 
    // numToEng(909) ➞ "nine hundred nine”

// Notes
// There are no hyphens used (e.g. "thirty five" not "thirty-five").
// The word "and" is not used (e.g. "one hundred one" not "one hundred and one").

const zeroToNineteen = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];

const zeroToMultiplesOfTen = ["zero", "ten", "twenty", "thirty", "forty",
"fifty", "sixty", "seventy", "eighty", "ninety"];

const numberToWords = (number, words = []) => {
    if (number == 0) {
        if (words.length) {
            return words.join(' ');
        }
        else {
            "zero";
        }
    }

    if (number < 20) {
        words.push(zeroToNineteen[number]);
        return numberToWords(0, words);
    }

    else if (number < 100) {
        words.push(zeroToMultiplesOfTen[Math.floor(number / 10)]);
        return numberToWords(number % 10, words);
    }
    
    else if (number < 1000) {
        words.push(numberToWords(Math.floor(number / 100)) + ' hundred');
        return numberToWords(number % 100, words);
    }
};

numberToWords(0)
// ➞ "zero" 
numberToWords(18)
// ➞ "eighteen"
numberToWords(47)
// ➞ "forty seven"
numberToWords(126)
// ➞ "one hundred twenty six" 
numberToWords(909)
// ➞ "nine hundred nine”