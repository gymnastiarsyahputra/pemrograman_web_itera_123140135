import React from 'react';
import BookItem from './BookItem';
import './BookList.css';

const BookList = ({ books, onEdit, onDelete }) => {
  if (books.length === 0) {
    return <p className="empty-message">Belum ada buku. Silakan tambahkan buku baru!</p>;
  }

  return (
    <div className="book-list">
      {books.map((book) => (
        <BookItem
          key={book.id}
          book={book}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
};

export default BookList;