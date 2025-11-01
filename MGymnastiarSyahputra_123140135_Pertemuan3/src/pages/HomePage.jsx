import React, { useState, useMemo } from 'react';
import BookList from '../components/BookList/BookList';
import BookForm from '../components/BookForm/BookForm';
import BookFilter from '../components/BookFilter/BookFilter';
import { useBooks } from '../context/BookContext';

const HomePage = () => {
  const { books, deleteBook } = useBooks();
  const [currentBook, setCurrentBook] = useState(null);
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [statusFilter, setStatusFilter] = useState('semua');

  const handleEdit = (book) => {
    setCurrentBook(book);
    setIsFormVisible(true);
  };

  const handleAddNew = () => {
    setCurrentBook(null);
    setIsFormVisible(true);
  };

  const handleFormClose = () => {
    setIsFormVisible(false);
    setCurrentBook(null);
  };

  const filteredBooks = useMemo(() => {
    return books
      .filter((book) => {
        return statusFilter === 'semua' || book.status === statusFilter;
      })
      .filter((book) => {
        const term = searchTerm.toLowerCase();
        return (
          book.title.toLowerCase().includes(term) ||
          book.author.toLowerCase().includes(term)
        );
      });
  }, [books, searchTerm, statusFilter]);

  return (
    <div className="container">
      <h1>Manajemen Buku Pribadi</h1>
      {!isFormVisible && (
        <button onClick={handleAddNew} className="btn btn-primary add-new-btn">
          + Tambah Buku Baru
        </button>
      )}
      {isFormVisible && (
        <BookForm bookToEdit={currentBook} onFormClose={handleFormClose} />
      )}
      <BookFilter
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        statusFilter={statusFilter}
        setStatusFilter={setStatusFilter}
      />
      <BookList
        books={filteredBooks}
        onEdit={handleEdit}
        onDelete={deleteBook}
      />
    </div>
  );
};

export default HomePage;