from math import ceil

class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    def __init__(self, pages: int):
        self.pages: int = pages
        self.photos: list[list[str]] = [[] for _ in range(pages)]
    
    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))
    
    def add_photo(self, label: str):
        for page_number, page in enumerate(self.photos, 1):
            if len(page) < self.__class__.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {page_number} slot {len(page)}"
        return "No more free slots"
    
    def display(self) -> str:
        if self.pages <= 0:
            return
        PAGE_SEPARATOR = "-" * 11

        res = [PAGE_SEPARATOR]

        for page in self.photos:
            res.extend([" ".join("[]" for _ in page), PAGE_SEPARATOR])
        
        return "\n".join(res)

album = PhotoAlbum.from_photos_count(5)
print(album.photos, album.pages)
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

    
