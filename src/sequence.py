import re as re

class Sequence:
    """This is the class that will storage the raw sequence"""
    
    name = "" # This variable will storage the name of the sequence
    sequence = "" # The raw sequence

    # The constructor of the sequence:
    def __init__(name, sequence):
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
    def how_many_A():
        amount_A = 0

        for nucleotide in self.sequence:
            if (nucleotide == 'A'):
                amount_A += 1
        return amount_A

    def how_many_T():
        amount_T = 0

        for nucleotide in self.sequence:
            if(nucleotide == 'T'):
                amount_T += 1
        return amount_T

    def how_many_purines():
        return self.how_many_A() + self.how_many_T()

    #Pirimidines
    def how_many_C():
        amount_C  = 0

        for nucleotide in self.sequence:
            if(nucleotide == 'C'):
                amount_C += 1
        return amount_C

    def how_many_G():
        amount_G = 0

        for nucleotide in self.sequence:
            if(nucleotide == 'G'):
                amount_G += 1
        return amount_G

    def how_many_pirimidines():
        return self.how_many_C() + self.how_many_G()

    


