from logic.person import Author


class Document(object):
    """
    Class used to represent a Document
    """

    def __init__(self, id_document: int,
                 number_of_pages: int,
                 title: str = 'Title',
                 category: str = 'Category', authors: list = []):
        """ Document constructor object.

                :param id_document: id of document.
                :type id_document: int
                :param number_of_pages: number of document's pages.
                :type number_of_pages: int
                :param title: title of the document.
                :type title: str
                :param category: represent the document's category
                :type category: str
                :returns: Document object
                :rtype: object
                """
        self._id_document = id_document
        self._title = title
        self._number_of_pages = number_of_pages
        self._category = category
        self._authors = authors

    @property
    def authors(self) -> list:
        return self._authors

    @authors.setter
    def authors(self, authors: list):
        for i in range (len(authors)):
            authors.append(Author())

    @property
    def id_document(self) -> int:
        """ Returns id of the document.
          :returns: document's id.
          :rtype: int
        """
        return self._id_document

    @id_document.setter
    def id_document(self, id_document: int):
        """ The id of the document.
        :param id_document: id of the document.
        :type: int
        """
        self._id_document = id_document

    @property
    def number_of_pages(self) -> int:
        """ Returns id of the document.
          :returns: document's id.
          :rtype: int
        """
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages: int):
        """ The id of the document.
        :param number_of_pages: number of document's pages.
        :type: int
        """
        self._number_of_pages = number_of_pages

    @property
    def title(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._title

    @title.setter
    def name(self, title: str):
        """ The name of the person.
        :param title: name of person.
        :type: str
        """
        self._title = title

    @property
    def category(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """ The last name of the person.
        :param category: last name of person.
        :type: str
        """
        self._category = category

    def __str__(self):
        """ Returns str of document.
          :returns: sting document
          :rtype: str
        """

        return '({0}, {1}, {2},{3})'.format(self.id_document, self.title, self.number_of_pages,self.category)


if __name__ == '__main__':
    authors_1 = [Author(123, 'Lucas', 'Mendoza'), Author(456, 'Maria', 'Mendez')]
    libro_1 = Document(id_document=73577376, number_of_pages=3, title="DSM 5", category="Musicological", authors=authors_1)
    for i in range (len(libro_1.authors)):
        print(libro_1.authors[i].id_person)
    print(libro_1)
