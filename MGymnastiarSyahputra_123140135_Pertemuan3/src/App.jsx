import React from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import HomePage from './pages/HomePage';
import StatsPage from './pages/StatsPage';
import { BookProvider } from './context/BookContext';
import './App.css';

function App() {
  return (
    <BookProvider>
      <Router>
        <header>
          <nav>
            <NavLink to="/" className={({isActive}) => (isActive ? 'active-link' : '')}>
              Beranda
            </NavLink>
            <NavLink to="/stats" className={({isActive}) => (isActive ? 'active-link' : '')}>
              Statistik
            </NavLink>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/stats" element={<StatsPage />} />
          </Routes>
        </main>
      </Router>
    </BookProvider>
  );
}

export default App;