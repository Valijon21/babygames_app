import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { App } from '../App';

describe('Bolajon Main App', () => {
  it('renders Bolajon title and navigation elements', () => {
    render(<App />);
    expect(screen.getByText('Bolajon')).toBeInTheDocument();
    expect(screen.getByText('Ta’limiy o‘yinlar')).toBeInTheDocument();
  });

  it('renders age filter options', () => {
    render(<App />);
    expect(screen.getByText('2–4 yosh')).toBeInTheDocument();
    expect(screen.getByText('5–7 yosh')).toBeInTheDocument();
    expect(screen.getByText('8–10 yosh')).toBeInTheDocument();
  });

  it('opens parental gate modal when parent button is clicked', () => {
    render(<App />);
    const parentBtn = screen.getByText('Ota-ona');
    fireEvent.click(parentBtn);
    expect(screen.getByText('Ota-onalar nazorati')).toBeInTheDocument();
  });
});
