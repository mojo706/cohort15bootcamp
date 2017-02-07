import unittest

from primeGen import primeGen

class TestPrimeNumber(unittest.TestCase):
    def functionOkay(self):
        self.prime = primeGen()

    def test_if_is_false_negative(self):
        """
        Test that negative numbers cannot be prime
        """
        result = primeGen(-10, -1)
        self.assertFalse(result, msg="Negative Numbers cannot have a prime!")

    def test_result_for_list_of_primes(self):
        result = primeGen(0, 15)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13] )

    def test_is_first_prime_2(self):
        result = primeGen(0, 15)
        firstPrime = result[0]
        self.assertEqual(firstPrime, 2)

    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        result = []
        if (sieve[i] === 4):
            result.append(i)
        self.assertFalse(result, msg='Four is not prime!')
    
    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(primeGen0(0,0))


if __name__=='__main__':
    unittest.main()
