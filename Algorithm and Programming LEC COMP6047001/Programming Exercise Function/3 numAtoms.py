"""
3. Write a function called num atoms() that calculates how many atoms are in n grams of an element given its atomic weight. This function should take two parameters: the amount of the element in grams and an optional argument representing the atomic weight of the element. The atomic weight of any particular element can be found on a periodic table but make the default value for the optional argument the atomic weight of gold (Au) 196.97 with units in grams/mole. A mole is a unit of measurement that is commonly used in chemistry to express an amount of a substance. Avogadro’s number is a constant, 6.022*10**23 atoms/mole, that can be used to find the number of atoms in a given sample. Use Avogadro’s number, the atomic weight, and the amount of the element in grams to find the number of atoms present in the sample. Your function should return this value.

The following demonstrates the proper behavior of this function using 10 grams and the atomic weight of gold (default), carbon, and hydrogen:

num_atoms(10)
3.0573183733563486e+22

num_atoms(10, 12.001)
5.017915173735522e+23

num_atoms(10, 1.008)
5.97420634920635e+24
"""
avogadro = 6.022 * 10 ** 23
def num_atoms(nAtom, wAtom = 196.97):       #default weight gold (atom) = 196.97
    totAtom = (nAtom / wAtom) * (avogadro)  #formula of total number of atoms
    print(f"{totAtom:.15e}")

num_atoms(10)
num_atoms(10, 12.001)
num_atoms(10, 1.008)