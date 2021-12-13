// JavaScript Practice 1: "Blood Types"

// Instructions:
// Please create your solutions with JavaScript Language and put it on your new repository. And send your repository link through this forum. Don't forget to add your name and class information in readme.md file
 
// Problems:
// When a person receives a blood transfusion, it is essential to make sure that the donor's blood type is compatible with the receiver's blood type. Receiving a blood type that is not compatible with your own can be life-threating, so blood banks always make sure to note the type of blood they receive from donors so that they can ensure a safe transfusion.
 
// Blood types are named according to three factors: presence of antigen A, presence of antigen B, and presence of Rh factor. 
// If antigen A is found, the blood type includes the letter "A". 
// If antigen B is found, the blood type includes the letter "B". 
// And if the Rh factor is present, the blood type ends with "+"; otherwise, it ends with "-". 
// If neither antigen A nor antigen B are found, the blood type includes the letter "O".
 
// For example, a person with only antigen A would have the blood type "A-". A person with both antigens A and B and the Rh factor would have blood type "AB+", and a person wih only the Rh factor would have blood type "O+".
 
// The rules for giving and receiving blood are as follows:
 
// A person with antigen A may only give blood to another person with antigen A.
// A person with antigen B may only give blood to another person with antigen B.
// A person with the Rh factor may only give blood to another person with the Rh factor.
// A person with none of the above factors (O-) can give blood to anyone.
// Write a function that takes in a donor's and receiver's blood types as strings and returns whether or not the donor can safely give blood to the receiver, according to the rules above.
 
// Examples
// canGiveBlood("O+", "A+") ➞ true
// canGiveBlood("A-", "B-") ➞ false
// canGiveBlood("A-", "AB+") ➞ true
 
// Notes
// All letters are capital.
// Each blood type will be one of the following strings: "O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-".

const canGiveBlood = (donorBlood, receiverBlood) => {
    let giveAntigenA = donorBlood.includes("A");
    let giveAntigenB = donorBlood.includes("B");
    let giveAntigenRH = donorBlood.includes("+");

    let getAntigenA = receiverBlood.includes("A");
    let getAntigenB = receiverBlood.includes("B");
    let getAntigenRH = receiverBlood.includes("+");
    
    if(giveAntigenA === true && getAntigenA === true){
        console.log("True");
    }
    else if(giveAntigenB === true && getAntigenB === true){
        console.log("True");
    }
    else if(giveAntigenRH === true && getAntigenRH === true){
        console.log("True");
    }
    else{
        console.log("False");
    }
}

canGiveBlood("O+", "A+")
canGiveBlood("A-", "B-")
canGiveBlood("A-", "AB+")