def support_reply(name, title=None):
    if title:
        prefix = title
    else:
        prefix = "Dear"
    
    return f"{prefix} {name}, we have resolved your issue."
