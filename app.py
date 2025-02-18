'''Python Classes: Custom Containers'''


class TagCloud:
    '''Initialize tags to an empty dict
    __tags is to private'''

    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        '''Adds tag attribute to dict if it doesn't exist, otherwise it increments by 1'''
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def _getitem__(self, tag):
        '''Gets a count of the tag attribute'''
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        '''Sets the tag count'''
        self.__tags[tag.lower()] = count

    def _len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
