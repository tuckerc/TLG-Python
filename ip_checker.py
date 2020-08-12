#!/usr/bin/env python3


# function for determining if ip is valid ipv4
def is_ipv4(input_ip):
    # get ip data
    ip_data = get_ip_data(input_ip)

    valid_length = 4

    # check basic validation
    if not passes_basic_validation(ip_data, valid_length):
        return False

    # validate each segment
    for segment in ip_data.get("bit_list"):
        if not len(segment) <= 3:
            return False
        for char in segment:
            if not 48 <= ord(char) <= 57:
                return False

    return True


# function for determining if ip is valid ipv6
def is_ipv6(input_ip):
    # get ip data
    ip_data = get_ip_data(input_ip)

    valid_length = 8

    # check basic validation
    if not passes_basic_validation(ip_data, valid_length):
        return False

    # validate each segment
    for segment in ip_data.get("bit_list"):
        if len(segment) != 4:
            return False
        for char in str(segment):
            if not 48 <= ord(char) <= 57 or not not 65 <= ord(char) <= 70:
                return False

    return True


# function to get ip data
def get_ip_data(input_ip):
    # dictionary for storing ip data
    ip_data = {"input_ip": input_ip}
    # determine if input_ip has dots
    has_dots(ip_data)
    # segment octets in list
    get_bits(ip_data)
    return ip_data


# function for determining if input_ip contains "."'s
def has_dots(ip_data):
    if not str(ip_data.get("input_ip")).__contains__("."):
        ip_data["contains_dot"] = False
    else:
        ip_data["contains_dot"] = True


# function to split bits from input ip
def get_bits(ip_data):
    ip_data["bit_list"] = bits_list = str(ip_data.get("input_ip")).strip().split(".")


# function for performing basic validation
def passes_basic_validation(ip_data, ip_len):
    # if input_ip does not contain ".", return False
    if not ip_data.get("contains_dot"):
        return False

    # if not 8 segments, return False
    if not len(ip_data.get("bit_list")) == ip_len:
        return False

    return True


print("This is a tool for validating IP addresses")


# keep going if user not finished
finished = False
while not finished:
    protocol = ""
    valid_protocol = False
    while not valid_protocol:
        # get protocol from user
        print("\nWhich IP protocol are you using?")
        print("\t1. IPv4")
        print("\t2. IPv6")
        protocol = input("")
        if protocol == "1":
            valid_protocol = True
            protocol = "IPv4"
        elif protocol == "2":
            valid_protocol = True
            protocol = "IPv6"

    # check IP using appropriate protocol
    if protocol == "IPv4":
        print("\nThis tool currently only supports decimal dot IPv4 format")
        # get ip from user
        ip = input("Enter an IP? ").strip()
        print(f"valid IP? {is_ipv4(ip)}")
    elif protocol == "IPv6":
        print("\nThis tool currently only supports hex dot IPv6 format")
        # get ip from user
        ip = input("Enter an IP? ").strip()
        print(f"valid IP? {is_ipv6(ip)}")

    # check if user finished
    yes_no = input("\nDo you need to check another IP? [(y)es / (n)o]")
    if yes_no.lower() not in ["y", "yes"]:
        finished = True
