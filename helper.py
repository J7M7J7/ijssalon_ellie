def onderstreep (tekst=""):
        uit = []
        uit.append(tekst)
        uit.append(len(tekst) * "=")
        return uit

# helper.py
def som(dictionary):
    return sum(dictionary.values())
