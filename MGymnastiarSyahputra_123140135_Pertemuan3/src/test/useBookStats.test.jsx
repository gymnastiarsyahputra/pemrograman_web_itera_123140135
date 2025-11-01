import { renderHook } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { useBookStats } from '../hooks/useBookStats';

describe('useBookStats', () => {
  it('calculates stats correctly', () => {
    const mockBooks = [
      { id: '1', status: 'milik' },
      { id: '2', status: 'milik' },
      { id: '3', status: 'baca' },
      { id: '4', status: 'beli' },
      { id: '5', status: 'beli' },
      { id: '6', status: 'beli' },
    ];

    const { result } = renderHook(() => useBookStats(mockBooks));

    expect(result.current.total).toBe(6);
    expect(result.current.owned).toBe(2);
    expect(result.current.reading).toBe(1);
    expect(result.current.wishlist).toBe(3);
  });
  
  it('returns zero for all stats when there are no books', () => {
    const mockBooks = [];
    
    const { result } = renderHook(() => useBookStats(mockBooks));

    expect(result.current.total).toBe(0);
    expect(result.current.owned).toBe(0);
    expect(result.current.reading).toBe(0);
    expect(result.current.wishlist).toBe(0);
  });
});