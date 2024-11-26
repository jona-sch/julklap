class NoPossibleJulklapMappingError(Exception):
    """
    Raised if no possible Julklap combination is available.
    2 possible causes: not enough people, or too strong exclusions.
    """
