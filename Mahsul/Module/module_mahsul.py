mahsul = []
total_amount = 0
total_count = 0


def get_document(product, price, count, person, storee):
    doc = {
        "PRODUCT": product,
        "PRICE": price,
        "COUNT": count,
        "PERSON": person,
        "STORE": storee,
    }
    return doc




def mahsul_transaction(doc_dic, total_amount, total_count):
    if doc_dic["STORE"] == "In":
        total_amount += doc_dic["PRICE"]
        total_count += doc_dic["COUNT"]
        mahsul.append(doc_dic)
    elif doc_dic["STORE"] == "Out":
        if doc_dic["COUNT"] == 0 or doc_dic["COUNT"] < total_count:
            return None
        else:
            total_count -= doc_dic["COUNT"]
            mahsul.append(doc_dic)
    return total_count
