class DataNotFoundError(Exception):
    def __init__(
        self,
        msg="Data Not Found",
        *args,
        **kwargs
    ):
        super().__init__(msg, *args, **kwargs)


balance = None

if not balance:
    raise Exception(DataNotFoundError)
response = {
    "valor_total": 100050
}
print(response)

