import React from 'react';
import './BookList.css';

const BookItem = ({ book, onEdit, onDelete }) => {
  const getStatusLabel = (status) => {
    switch (status) {
      case 'milik':
        return 'Dimiliki';
      case 'baca':
        return 'Dibaca';
      case 'beli':
        return 'Wishlist';
      default:
        return '';
    }
  };

  return (
    <div className="book-item">
      <div className="book-info">
        <h4>{book.title}</h4>
        <p>{book.author}</p>
      </div>
      <div className="book-details">
        <span className={`status-label status-${book.status}`}>
          {getStatusLabel(book.status)}
        </span>
        <div className="book-actions">
          <button onClick={() => onEdit(book)} className="btn-edit">
            Edit
          </button>
          <button onClick={() => onDelete(book.id)} className="btn-delete">
            Hapus
          </button>
        </div>
      </div>
    </div>
  );
};

export default BookItem;