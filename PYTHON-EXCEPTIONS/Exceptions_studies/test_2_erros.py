# ------ exceptions

from importlib_metadata import re


class UnauthorizedError(Exception):
    pass


class ForbiddenError(Exception):
    pass


class BadRequestError(Exception):
    pass


class InternalServerError(Exception):
    pass


class NoPath(Exception):
    pass


class NotFoundError(Exception):
    pass


# --------- functions

# name = "Renata"
# id = ""

# if name and id:
#     print("DATA: ", name, id)
# print(NotFoundError("THE DATA WASN'T FOUND"))


# -------- getting the key of a dict
# broker_note: str = "https://stackoverflow.com/questions/4591125"

# data: dict = {"pdf_link": broker_note}

# # print(data["pdf_link"])

# if not data["pdf_link"]:
#     raise NotFoundError({"pdf_link": "BROKER NOTE NOT FOUND"})
# print(data)


# -------- getting open_earnings_data
# open_earnings_data = "Earnings data"

# if not open_earnings_data:    
#     raise NotFoundError("Not Found Error: Data Not Found")
# print(open_earnings_data)


# -------- getting data from a string

# bmf_account = "123456"
# region = "BR"
# path_route = "https://stackoverflow.com/questions/4591125"

# path = f"{bmf_account}/{region}/{path_route}/"
# print(path)

# if bmf_account and region and path_route in path:
#     print("EVERYTHING OK", path)
# else:
#     raise NotFoundError("Not Found Error: Data Not Found") 


# -------- getting the files
# files_data = "142353673"

# if not files_data:
#     raise NotFoundError("NotFoundError: The Data was not Found")
# print(files_data) 


# error handler classes

class NotFoundDataError(Exception):

    @staticmethod
    def not_found_data():
        error_response = {"NotFoundError": "Data Not Found"}
        return error_response

balance = ""


if not balance:
    raise NotFoundError({"NotFoundError": "Data Not Found"})
else:
    print({'balance': balance})
