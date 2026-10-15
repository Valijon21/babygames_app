import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { ColoringGame } from '../features/coloring/ColoringGame';

describe('ColoringGame Component', () => {
  it('renders coloring title and back button', () => {
    const handleBack = vi.fn();
    const handleComplete = vi.fn();
    render(<ColoringGame onBack={handleBack} onComplete={handleComplete} />);

    expect(screen.getByText('🎨 Quvnoq Mushukcha')).toBeInTheDocument();
    expect(screen.getByText('Orqaga')).toBeInTheDocument();
  });

  it('renders SVG canvas with clickable regions', () => {
    const { container } = render(<ColoringGame onBack={vi.fn()} onComplete={vi.fn()} />);
    const svg = container.querySelector('svg');
    expect(svg).toBeInTheDocument();
  });

  it('clicking reset button opens confirmation dialog', () => {
    render(<ColoringGame onBack={vi.fn()} onComplete={vi.fn()} />);
    const resetBtn = screen.getByLabelText('Tozalash');
    fireEvent.click(resetBtn);

    expect(screen.getByText('Rasmni tozalaymizmi?')).toBeInTheDocument();
  });
});
