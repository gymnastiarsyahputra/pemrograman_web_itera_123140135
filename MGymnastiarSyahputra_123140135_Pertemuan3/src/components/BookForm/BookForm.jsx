import React, { useState, useEffect } from 'react';
import { useBooks } from '../../context/BookContext';
import './BookForm.css';

const BookForm = ({ bookToEdit, onFormClose }) => {
  const [book, setBook] = useState({ title: '', author: '', status: 'milik' });
  const [errors, setErrors] = useState({});
  const { addBook, updateBook } = useBooks();

  useEffect(() => {
    if (bookToEdit) {
      setBook(bookToEdit);
    } else {
      setBook({ title: '', author: '', status: 'milik' });
    }
  }, [bookToEdit]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setBook({ ...book, [name]: value });
  };

  const validate = () => {
    let tempErrors = {};
    if (!book.title) tempErrors.title = 'Judul tidak boleh kosong.';
    if (!book.author) tempErrors.author = 'Penulis tidak boleh kosong.';
    setErrors(tempErrors);
    return Object.keys(tempErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      if (book.id) {
        updateBook(book);
      } else {
        addBook(book);
      }
      onFormClose(); // Menutup form setelah submit
    }
  };

  return (
    <form onSubmit={handleSubmit} className="book-form">
      <h3>{book.id ? 'Edit Buku' : 'Tambah Buku Baru'}</h3>
      <div className="form-group">
        <label>Judul</label>
        <input
          type="text"
          name="title"
          value={book.title}
          onChange={handleChange}
          placeholder="e.g., Laskar Pelangi"
        />
        {errors.title && <p className="error">{errors.title}</p>}
      </div>
      <div className="form-group">
        <label>Penulis</label>
        <input
          type="text"
          name="author"
          value={book.author}
          onChange={handleChange}
          placeholder="e.g., Andrea Hirata"
        />
        {errors.author && <p className="error">{errors.author}</p>}
      </div>
      <div className="form-group">
        <label>Status</label>
        <select name="status" value={book.status} onChange={handleChange}>
          <option value="milik">Dimiliki</option>
          <option value="baca">Sedang Dibaca</option>
          <option value="beli">Ingin Dibeli</option>
        </select>
      </div>
      <div className="form-actions">
        <button type="submit" className="btn btn-primary">
          {book.id ? 'Simpan Perubahan' : 'Tambah Buku'}
        </button>
        <button type="button" className="btn" onClick={onFormClose}>
          Batal
        </button>
      </div>
    </form>
  );
};

export default BookForm;