class PaginationError(BaseException):
    pass


class CustomPaginator:
    """
    The paginator accepts a list with data. On initialization,
    it parses the list and writes to memory the number of pages, the next page, and the previous page.
    It also returns a new list of records that match the given slice.
    """
    page_item_count = 10

    def __init__(self, page: int, iter_obj: list, per_page: int = None):
        self.array = iter_obj
        self.per_page = self.page_item_count
        if per_page:
            self.per_page = per_page
        self.total_pages = self._get_total_pages()
        if page > self.total_pages or page < 1:
            raise PaginationError
        self.page = page
        self.previous_page = self._get_previous_page()
        self.next_page = self._get_next_page()

    def _get_previous_page(self):
        if self.page == 1:
            return None
        elif 1 < self.page <= self.total_pages:
            return self.page - 1

    def _get_next_page(self):
        if self.total_pages > 1:
            if self.page == self.total_pages:
                return None
            return self.page + 1
        return self.page

    def _get_total_pages(self):
        n = len(self.array) / self.per_page
        if int(n) == n:
            return int(n)
        return int(n) + 1

    def __len__(self):
        return self.total_pages

    def has_next_page(self):
        if self.next_page:
            return True
        return False

    def has_previous_page(self):
        if self.previous_page:
            return True
        return False

    def get_data(self):
        return self.array[self.per_page * self.page - self.per_page:self.per_page * self.page]


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    pag = CustomPaginator(2, data, 10)
    print(pag.total_pages, 'total')
    print(pag.next_page, 'next')
    print(pag.has_next_page(), 'has next')
    print(pag.previous_page, 'prev')
    print(pag.has_previous_page(), 'has prev')
    print(pag.get_data())
