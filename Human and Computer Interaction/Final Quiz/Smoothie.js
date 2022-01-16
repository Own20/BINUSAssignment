// Create a class Smoothie and do the following:
    // Create a constructor property called ingredients.
    // Create a getCost method which calculates the total cost of the ingredients used to make the smoothie.
    // Create a getPrice method which returns the number from getCost plus the number from getCost multiplied by 1.5. Round to two decimal places.
    // Create a getName method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". 

// Ingredients      Price
// Strawberries     $1.50
// Banana           $0.50
// Mango            $2.50
// Blueberries      $1.00
// Raspberries      $1.00
// Apple            $1.75
// Pineapple        $3.50

// Examples
    // s1 = new Smoothie(["Banana"]) 
    // s1.ingredients ➞ ["Banana"] 
    // s1.getCost() ➞ "$0.50" 
    // s1.getPrice() ➞ "$1.25" 
    // s1.getName() ➞ "Banana Smoothie"

    // s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"]) 
    // s2.ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"] 
    // s2.getCost() ➞ "$3.50" 
    // s2.getPrice() ➞ "$8.75" 
    // s2.getName() ➞ "Blueberry Raspberry Strawberry Fusion"

const Ingredients = (ingredient) => {
    Ingredients = ["Strawberries", "Banana", "Mango", "Blueberries", "Raspberries", "Apple", "Pineapple"]
    Price = [1.50, 0.50, 2.50, 1.00, 1.00, 1.75, 3.50]

    let ingredient = []
    let price = 0
    let smoothie = key.toString()

    let getCost = 0

    for (let i = 0; i < Ingredients; i++) {    
        Ingredients.push(ingredient[i] - smoothie.charAt(price));
        price++;
        if (price == smoothie.length) {
            price = 0;
        }
    }

    let getPrice = round()
}