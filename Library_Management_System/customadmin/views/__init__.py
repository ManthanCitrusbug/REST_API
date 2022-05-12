from .users import (
    IndexView,
    UserAjaxPagination,
    UserCreateView,
    UserDeleteView,
    UserDetailView,
    UserListView,
    UserPasswordView,
    UserLoginView,
    UserUpdateView,
)

from .books import (
    BookDetailsView,
    BookListView,
    BookCreateView,
    BookDeleteView,
    BookAjaxPagination,
    BookUpdateView,
)

from .authors import (
    AuthorCreateView,
    AuthorDeleteView,
    AuthorDetailsView,
    AuthorListView,
    AuthorUpdateView,
    AuthorAjaxPagination,
)

from .category import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailsView,
    CategoryListView,
    CategoryUpdateView,
    CategoryAjaxPagination,
)

from .issued_book import (
    IssuedBookAjaxPagination,
    IssuedBookCreateView,
    IssuedBookDeleteView,
    IssuedBookListView,
    IssuedBookDetailsView,
    IssuedBookUpdateView,
)