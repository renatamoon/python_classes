from datetime import datetime

# ----- Exceptions

class NoPath(Exception):
    pass


class NotFoundError(Exception):
    pass


# ----------------- function to get the pdf path

client_id: str = '1234'
start_date: str = '2022-03-22'
end_date: str = '2022-04-22'


# -------- Validation of the data

path = f"{client_id}/statements/{start_date}-{end_date}.pdf"
    
if client_id and start_date and end_date in path:
    if path:
        print(f"This is a path, {path}")
else:
    raise NotFoundError('Data Not Found')


# ------------- function to get the pdf link

link: str = "https://stackoverflow.com/questions/4591125"
link_pdf: dict = {"pdf_link": link}

print(link_pdf)

if link:
    print(link_pdf)
else:
    raise NotFoundError({"pdf_link": "PDF Not Found"})