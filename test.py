from nyt_request import transform_hours, request


def main():
    date = '2017/01/01'
    response = request('51505e1b122b4e04953306674b56797e', 'business day', transform_hours(date))


if __name__ == '__main__':
    main()
