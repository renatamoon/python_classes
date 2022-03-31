from enum import Enum

from pyparsing import Or


class OrderTifs(Enum):
    GOOD_TILL_CANCEL = "GTC"
    DAY = "DAY"
    IMMEDIATE_OR_CANCEL = "IOC"
    FILL_OR_KILL = "FOK"
    GOOD_TILL_DATE = "GTD"
    AT_THE_CLOSE = "ATC"
    GOOD_FOR_AUCTION = "GFA"
    NOT_AVAILABLE = "NA"

    @classmethod
    def has_member_value(cls, value):
        return cls.__members__.get(value)



def get_tiff_response_acronimun(tif_value: str):
    tiff_response = OrderTifs.has_member_value(value=tif_value)    
    if tiff_response is not None:
        return tiff_response.value
    not_available = OrderTifs.NOT_AVAILABLE       
    return not_available.value
    

new = get_tiff_response_acronimun("GOOD_TILL_CANCEL")
print(new)
