from nyt_request import transform_hours, request


def main():
    date = '2017/01/01'
    api_key = '51505e1b122b4e04953306674b56797e'
    section = 'business day'

    request(api_key, section, transform_hours(date))


if __name__ == '__main__':
    main()
