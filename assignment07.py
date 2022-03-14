#------------------------------------------#
# Title: assignment07.py
# Desc: Modified Script for Assignment 07
# Change Log: (Who, When, What)
# DBiesinger, 2022-Jan-01, Created File
# Yuguan Pan, 2022-Mar-13, Modefied script
# Yuguan Pan, 2022-Mar-13, Keep modifing script
#------------------------------------------#

# -- DATA -- #
strFileInput = 'mathIn.txt'
strFileOutput = 'mathOut.txt'

# -- PROCESSING -- #
class SimpleMath:
    """A collection of simple math processing functions """

    @staticmethod
    def get_sum(val1 = 0.0, val2 = 0.0):
        """Function for adding two values


        Args:
            val1: the first number to add
            val2: the second number to add


        Returns:
            A float corresponding to the sum of val1 and val2
        """
        return float(val1 + val2)

    @staticmethod
    def get_diffference(val1 = 0.0, val2 = 0.0):
        """Function for subtracting two values


        Args:
            val1: the number to subtract from
            val2: the number to subtract


        Returns:
            A float corresponding to the difference of val1 and val2
        """
        return float(val1 - val2)

    @staticmethod
    def get_product(val1 = 0.0, val2 = 0.0):
        """Function for multiplying two values


        Args:
            val1: the first number to multiply
            val2: the second number to multiply


        Returns:
            A float corresponding to the product of val1 and val2
        """
        return float(val1 * val2)

    @staticmethod
    def get_quotient(val1 = 0.0, val2 = 0.0):
        """Function for dividing two values


        Args:
            val1: the number to divide
            val2: the number to divide by


        Returns:
            A float corresponding to the quotient of val1 and val2
        """
        return float(val1 / val2)


class IO:
    """A collection of the Input / Output operations """

    def read_file(fileName):
        """
        function to read in two numbers from file fileName and return these

        Args:
            fileName (string): file name to read the numbers from

        Returns:
            numA (int): first number in file fileName.
            numB (int): second number in file fileName.

        """
        
        objFile = open(fileName, 'r')
        cnt = 0
        for line in objFile:
            if cnt == 1:
                raise Exception("Please only input one row")
            try: 
                NumA, NumB = line.strip().split(',')
            except: 
                raise Exception("Please enter 2 numbers separated by comma")
            cnt = cnt + 1
        objFile.close()
        
        try: 
            intNumA = int(NumA)
            intNumB = int(NumB)
        except:
            raise Exception("Please input integers")
        
        if intNumB == 0:
            raise Exception("Denominator cannot be 0")
        return intNumA, intNumB

        

    def write_file(fileName, results):
        """
        function to write the math results to file fileName

        Args:
            fileName (string): file Name to write the results to.
            results (list): The results

        Returns:
            None.

        """
        objFile = open(fileName, 'w')
        objFile.write("Sum: " + str(results[0]) + '\n')
        objFile.write("Difference: " + str(results[1]) + '\n')
        objFile.write("Product: " + str(results[2]) + '\n')
        objFile.write("Quotient: " + str(results[3]) + '\n')
        objFile.close()
       

# -- PRESENTATION (Input/Output) -- #
print('Basic Math script. Calculating the Sum, Difference, Product and Quotient of two numbers.')
intNumA, intNumB = IO.read_file(strFileInput)
lstResults = []
lstResults.append(SimpleMath.get_sum(intNumA, intNumB))
lstResults.append(SimpleMath.get_diffference(intNumA, intNumB))
lstResults.append(SimpleMath.get_product(intNumA, intNumB))
lstResults.append(SimpleMath.get_quotient(intNumA, intNumB))
IO.write_file(strFileOutput, lstResults)


