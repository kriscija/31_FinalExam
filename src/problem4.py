"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Joe Krisciunas.  May 2018.

"""  # DoneTODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# DoneTODO: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------
    bigboy = Pig(5000000)
    slimboy = Pig(1)
    porker = Pig(30)
    print(porker.weight)
    print(porker.get_weight())
    porker.eat(500)
    print(porker.get_weight())
    porker.eat_for_a_year()
    print(porker.get_weight())
    test1 = porker.heavier_pig(bigboy)
    print(test1.weight)
    test2 = porker.heavier_pig(slimboy)
    print(test2.weight)
    test3 = porker.new_pig(bigboy)
    print(test3.weight)
    test4 = porker.new_pig(slimboy)
    print(test4.weight)


class Pig(object):
    def __init__(self, weight):
        self.weight = weight
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        # DoneTODO: Implement and test this method.

    def get_weight(self):
        """ Returns this Pig's weight. """
        return self.weight
        # DoneTODO: Implement and test this method.

    def eat(self, pounds_of_slop):
        self.weight = self.weight+ pounds_of_slop
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        # DoneTODO: Implement and test this method.

    def eat_for_a_year(self):
        self.eat(365)
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # DoneTODO: Implement and test this method.

    def heavier_pig(self, other_pig):
        if self.weight > other_pig.weight:
            return self
        else:
            return other_pig
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        # DoneTODO: Implement and test this method.

    def new_pig(self, other_pig):
        if self.weight > other_pig.weight:
            nupig = Pig(self.weight)
            return nupig
        else:
            nupig = Pig(other_pig.weight)
            return nupig
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        # DoneTODO: Implement and test this method.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
