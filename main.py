import re


def main():
    regex = r"(10:[0-5][0-9]:[0-5][0-9]).+( [4-5][0-9][0-9]).+"
    file = open('access.log.txt', mode='r')
    log_failures = file.read()
    failures = re.findall(regex, log_failures)
    print(failures)
    print("Number of failed requests: ", len(failures))


if __name__ == '__main__':
    main()
