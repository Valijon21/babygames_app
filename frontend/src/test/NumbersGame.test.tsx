import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { NumbersGame } from '../features/numbers/NumbersGame';

describe('NumbersGame Component', () => {
  it('renders counting prompt and options', () => {
    render(<NumbersGame onBack={vi.fn()} onComplete={vi.fn()} />);

    expect(screen.getByText('🔢 1 dan 10 gacha sanash')).toBeInTheDocument();
    expect(screen.getByText('Nechta quvnoq olma bor?')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: '3' })).toBeInTheDocument();
  });

  it('tapping item displays counted number indicator', () => {
    render(<NumbersGame onBack={vi.fn()} onComplete={vi.fn()} />);
    const apples = screen.getAllByRole('button').filter((b) => b.textContent?.includes('🍎'));
    expect(apples.length).toBe(3);

    fireEvent.click(apples[0]);
    expect(apples[0].textContent).toContain('1');
  });

  it('clicking correct option triggers positive feedback', () => {
    render(<NumbersGame onBack={vi.fn()} onComplete={vi.fn()} />);
    const correctBtn = screen.getByRole('button', { name: '3' });
    fireEvent.click(correctBtn);

    expect(screen.getByText('To‘g‘ri! Barakalla! 🎉')).toBeInTheDocument();
  });
});
