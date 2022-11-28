import requests as r

base_url = "https://api.truthordarebot.xyz/api/"


def truth(rating=None):

    if rating is not None:
        if rating.upper() in ["PG", "PG13", "R"]:
            response = r.get(base_url + "truth" + f"?rating={rating.upper()}")
        else:
            response = r.get(base_url + "truth")

    elif rating is None:
        response = r.get(base_url + "truth")

    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(
            "There was an error while fetching that request from the API please try again later."
        )


def dare(rating=None):

    if rating is not None:
        if rating.upper() in ["PG", "PG13", "R"]:
            response = r.get(base_url + "dare" + f"?rating={rating.upper()}")
        else:
            response = r.get(base_url + "dare")

    elif rating is None:
        response = r.get(base_url + "dare")

    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(
            "There was an error while fetching that request from the API please try again later."
        )


def wyr(rating=None):

    if rating is not None:
        if rating.upper() in ["PG", "PG13", "R"]:
            response = r.get(base_url + "wyr" + f"?rating={rating.upper()}")
        else:
            response = r.get(base_url + "wyr")

    elif rating is None:
        response = r.get(base_url + "wyr")

    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(
            "There was an error while fetching that request from the API please try again later."
        )


def nhie(rating=None):

    if rating is not None:
        if rating.upper() in ["PG", "PG13", "R"]:
            response = r.get(base_url + "nhie" + f"?rating={rating.upper()}")
        else:
            response = r.get(base_url + "nhie")

    elif rating is None:
        response = r.get(base_url + "nhie")

    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(
            "There was an error while fetching that request from the API please try again later."
        )


def paranoia(rating=None):

    if rating is not None:
        if rating.upper() in ["PG", "PG13", "R"]:
            response = r.get(base_url + "paranoia" + f"?rating={rating.upper()}")
        else:
            response = r.get(base_url + "paranoia")

    elif rating is None:
        response = r.get(base_url + "paranoia")

    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(
            "There was an error while fetching that request from the API please try again later."
        )
