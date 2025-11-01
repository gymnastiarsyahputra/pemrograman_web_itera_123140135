import React from 'react';
import { useBooks } from '../context/BookContext';
import { useBookStats } from '../hooks/useBookStats';
import './StatsPage.css';

const StatsPage = () => {
  const { books } = useBooks();
  const { total, owned, reading, wishlist } = useBookStats(books);

  return (
    <div className="container">
      <h1>Statistik Buku</h1>
      <div className="stats-grid">
        <div className="stat-card">
          <h2>{total}</h2>
          <p>Total Buku</p>
        </div>
        <div className="stat-card">
          <h2>{owned}</h2>
          <p>Dimiliki</p>
        </div>
        <div className="stat-card">
          <h2>{reading}</h2>
          <p>Sedang Dibaca</p>
        </div>
        <div className="stat-card">
          <h2>{wishlist}</h2>
          <p>Ingin Dibeli</p>
        </div>
      </div>
    </div>
  );
};

export default StatsPage;