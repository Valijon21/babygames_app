import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { AlphabetGame } from '../features/alphabet/AlphabetGame';

describe('AlphabetGame Component', () => {
  it('renders alphabet title, letter display, and phonetic word', () => {
    render(<AlphabetGame onBack={vi.fn()} onComplete={vi.fn()} />);

    expect(screen.getByText('🔤 O‘zbek Alifbosi')).toBeInTheDocument();
    expect(screen.getByText('Anor')).toBeInTheDocument();
  });

  it('allows clicking different letters to switch character', () => {
    render(<AlphabetGame onBack={vi.fn()} onComplete={vi.fn()} />);
    const bButton = screen.getByRole('button', { name: 'B' });
    fireEvent.click(bButton);

    expect(screen.getByText('Baliq')).toBeInTheDocument();
  });

  it('renders handwriting tracing canvas', () => {
    const { container } = render(<AlphabetGame onBack={vi.fn()} onComplete={vi.fn()} />);
    const canvas = container.querySelector('canvas');
    expect(canvas).toBeInTheDocument();
  });
});
