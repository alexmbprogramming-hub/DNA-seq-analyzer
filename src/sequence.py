import re as re

class Sequence:
    """This is the class that will storage the raw sequence"""
    
    name = "" # This variable will storage the name of the sequence
    sequence = "" # The raw sequence

    # The constructor of the sequence:
    def __init__(self, name, sequence):
        sequence = sequence.upper()

        if not re.fullmatch(r"^[ACTG]+$", sequence):
            raise ValueError("DNA sequence just will accept ATCG")
        self.sequence = sequence

        # The constructor will accept as name strings containing only alphanumeric characters or underscore _ character
        if not re.fullmatch(r"^[\w]+", name):
            raise ValueError("The sequence name can contain just alphanumerics characters or '_'")
        self.name = name

    # Read the quantities of each nucleotide

    # Purines
    def how_many_A(self):
        amount_A = 0

        for nucleotide in self.sequence:
            if (nucleotide == 'A'):
                amount_A += 1
        return amount_A

    def how_many_T(self):
        amount_T = 0

        for nucleotide in self.sequence:
            if(nucleotide == 'T'):
                amount_T += 1
        return amount_T

    def how_many_purines(self):
        return self.how_many_A() + self.how_many_T()

    #Pirimidines
    def how_many_C(self):
        amount_C  = 0

        for nucleotide in self.sequence:
            if(nucleotide == 'C'):
                amount_C += 1
        return amount_C

    def how_many_G(self):
        amount_G = 0

        for nucleotide in self.sequence:
            if(nucleotide == 'G'):
                amount_G += 1
        return amount_G

    def how_many_pirimidines(self):
        return self.how_many_C() + self.how_many_G()

    # Percentages:
    def percentage_purines(self):
        return self.how_many_purines() / len(self.sequence) * 100

    def percentage_pirimidines(self):
        return self.how_many_pirimidines() / len(self.sequence) * 100

    # Complementary string
    def complementary_string(self):
        complementary_string = ""
        for i in self.sequence:
            if i == 'A':
                complementary_string = 'T' + complementary_string
            elif i == 'T':
                complementary_string = 'A' + complementary_string
            elif i == 'C':
                complementary_string = 'G' + complementary_string
            elif i == 'G':
                complementary_string = 'C' + complementary_string
            else:
                raise ValueError("The sequence cannot have a character diferent from ATCG")
        return complementary_string
            

    # Return full data:
    """
    The next function will return
    a list that will contain the full data
    of the sequence in the next order:
    name, sequence
    number of A, of T, of G of C,
    percentage of AT, precentage of CG
    reverse sequence
    """
    def full_data_list(self):
        full_data_list = [self.name, self.sequence, self.how_many_A(),
                          self.how_many_T(), self.how_many_G(),
                          self.how_many_C(), self.percentage_purines(),
                          self.percentage_pirimidines(), self.complementary_string()]
        return full_data_list