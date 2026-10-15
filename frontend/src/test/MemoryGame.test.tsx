import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { MemoryGame } from '../features/memory/MemoryGame';

describe('MemoryGame Component', () => {
  it('renders memory game title, move counter, and 8 card slots', () => {
    render(<MemoryGame onBack={vi.fn()} onComplete={vi.fn()} />);

    expect(screen.getByText('🧠 Xotira o‘yini')).toBeInTheDocument();
    expect(screen.getByText(/Urinish: 0/i)).toBeInTheDocument();

    const questionMarks = screen.getAllByText('❓');
    expect(questionMarks.length).toBe(8);
  });

  it('clicking card flips it and increments move counter on pair selection', () => {
    render(<MemoryGame onBack={vi.fn()} onComplete={vi.fn()} />);
    const cardButtons = screen.getAllByRole('button').filter((b) => b.textContent?.includes('❓'));

    fireEvent.click(cardButtons[0]);
    fireEvent.click(cardButtons[1]);

    expect(screen.getByText(/Urinish: 1/i)).toBeInTheDocument();
  });
});
