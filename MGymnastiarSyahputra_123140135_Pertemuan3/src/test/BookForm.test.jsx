import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import BookForm from '../components/BookForm/BookForm';
import { BookProvider } from '../context/BookContext'; // Wrap with provider

// Mock onFormClose prop
const mockOnFormClose = vi.fn();

describe('BookForm', () => {
  it('renders correctly for adding a new book', () => {
    render(
      <BookProvider>
        <BookForm onFormClose={mockOnFormClose} />
      </BookProvider>
    );
    expect(screen.getByText('Tambah Buku Baru')).toBeInTheDocument();
    expect(screen.getByLabelText('Judul')).toBeInTheDocument();
    expect(screen.getByLabelText('Penulis')).toBeInTheDocument();
  });

  it('shows error messages for empty fields on submit', () => {
    render(
      <BookProvider>
        <BookForm onFormClose={mockOnFormClose} />
      </BookProvider>
    );

    fireEvent.click(screen.getByText('Tambah Buku'));
    
    expect(screen.getByText('Judul tidak boleh kosong.')).toBeInTheDocument();
    expect(screen.getByText('Penulis tidak boleh kosong.')).toBeInTheDocument();
  });

  it('renders with existing book data when editing', () => {
    const bookToEdit = { id: '1', title: 'Test Book', author: 'Test Author', status: 'baca' };
    render(
      <BookProvider>
        <BookForm bookToEdit={bookToEdit} onFormClose={mockOnFormClose} />
      </BookProvider>
    );

    expect(screen.getByText('Edit Buku')).toBeInTheDocument();
    expect(screen.getByLabelText('Judul')).toHaveValue('Test Book');
    expect(screen.getByLabelText('Penulis')).toHaveValue('Test Author');
    expect(screen.getByLabelText('Status')).toHaveValue('baca');
  });
});