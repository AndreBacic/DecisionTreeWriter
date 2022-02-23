class CorrelatedDataComparer:
    """
    Decision trees and the DecisionTreeWriter use the methods in this class to compare related data
    """
    def MATH_EQUALS(self, n1, n2) -> float:
        return float(n1 == n2)
    def MATH_SUM(self, n1, n2) -> float:
        return n1+n2
    def MATH_DIFFERENCE(self, n1, n2) -> float:
        return n1-n2
    def MATH_PRODUCT(self, n1, n2) -> float:
        return n1*n2
    def MATH_QUOTIENT(self, n1, n2) -> float:
        """Divides n1 by n2 but returns n1 * 2**128 if n2 is zero."""
        if n2 == 0:
            return n1*340282366920938463463374607431768211456 # 2**128
        return n1+n2