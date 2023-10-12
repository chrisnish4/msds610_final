## Author: Sai Vamsi Pujari

import re
import datetime
import argparse
from urllib.parse import urlparse


def count_vowels(string):
    return sum(1 for char in string if char.lower() in "aeiou")


def strip_vowels(string):
    vowels = ["a", "i", "e", "o", "u"]
    response = []
    for c in string.lower():
        if not c in vowels and c != " ":
            response.append(c)

    return "".join(response)


def extract_domain(url):
    parsed_url = urlparse(url)
    # Split the subdomain from the netloc (domain)
    subdomain = parsed_url.netloc.split(".")[1]
    return subdomain


def print_state(state):
    print(f"INFO: update : {state}")


def get_a_password(given_name, last_name):
    vowels = ["a", "i", "e", "o", "u"]
    full_name = f"{given_name} {last_name}".lower()
    nwords = len(full_name.split())
    nvowels = count_vowels(full_name)

    print(f"Found {nvowels} vowels in the given and last name")

    curr_date = datetime.datetime.now().day

    l1_str = list(strip_vowels(full_name))

    print_state(strip_vowels(full_name))

    if nwords < len(l1_str):
        l1_str[nwords] = l1_str[nwords].upper()
        print_state("".join(l1_str))

    if nvowels < len(l1_str):
        l1_str[nvowels] = l1_str[nvowels].upper()
        print_state("".join(l1_str))
    else:
        l1_str.append(str(nvowels))
        l1_str.append(chr(curr_date * nvowels))

    return "".join(l1_str[::-1])


# get_a_password("Sai Vamsi", "Pujari")


def get_strong_password(
    given_name="Sai Vamsi",
    last_name="Pujari",
    url=None,  # "www.meta.com",
    dob=None,  # "01-01-1900",
):
    baseline_password = get_a_password(given_name, last_name)

    if url is None and dob is None:
        print("Generating a password of strength: moderate ...")
        return baseline_password, 0

    url = url if url.startswith("https://") else "https://" + url
    org_name = extract_domain(url)

    strong_password = (
        baseline_password + ":" + "".join(set(strip_vowels(org_name)[::-1]))
    )

    dob_sum = sum(int(char) for char in dob if char.isdigit())
    extra_char = "\." if dob_sum % 2 == 0 else "/."

    return strong_password + str(dob_sum % 10) + extra_char, 1


# get_strong_password(
#     given_name="Sai Vamsi", last_name="Pujari", url="www.meta.com"
# )


# function_with_args.py


def main():
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument(
        "--given_name",
        type=str,
        required=True,
        help="provide givenname either 'firstname' or 'firstname middlename'",
    )
    parser.add_argument(
        "--last_name", type=str, required=True, help="provide last name"
    )
    parser.add_argument(
        "--url", type=str, default=None, help="provide url of the website"
    )
    parser.add_argument(
        "--dob",
        type=str,
        default=None,
        help="date of birth or date of interset in 'MM-DD-YYYY'",
    )
    args = parser.parse_args()
    response, level = get_strong_password(
        args.given_name, args.last_name, args.url, args.dob
    )

    strength = ["moderate", "strong"]

    print(f"Generated passcode: {response} \nStrength: {strength[level]}")


if __name__ == "__main__":
    main()


# generate_password.py --given_name 'Sai Vamsi' --last_name 'Pujari'
# generate_password.py --given_name 'Sai Vamsi' --last_name 'Pujari' --url 'www.meta.com' --dob '11-11-1900'
